from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import torch.nn as nn

app = Flask(__name__)
CORS(app)

# ================= ROOT ROUTE =================

@app.route("/")
def home():
    return "Backend is running 🚀"

# ================= MODEL DEFINITION =================

class ChromatinCNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv = nn.Sequential(
            nn.Conv1d(4, 32, kernel_size=10),
            nn.ReLU(),
            nn.MaxPool1d(2),

            nn.Conv1d(32, 64, kernel_size=10),
            nn.ReLU(),
            nn.MaxPool1d(2),

            nn.Conv1d(64, 128, kernel_size=10),
            nn.ReLU(),
            nn.MaxPool1d(2)
        )

        with torch.no_grad():
            dummy = torch.zeros(1, 4, 4000)
            dummy_out = self.conv(dummy)
            self.flat_dim = dummy_out.view(1, -1).shape[1]

        self.fc = nn.Sequential(
            nn.Linear(self.flat_dim * 2, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 1)
        )

    def forward(self, x1, x2):
        x1 = self.conv(x1)
        x2 = self.conv(x2)

        x1 = torch.flatten(x1, 1)
        x2 = torch.flatten(x2, 1)

        x = torch.cat((x1, x2), dim=1)

        return self.fc(x)

# ================= LOAD MODEL =================

model = ChromatinCNN()
model.load_state_dict(torch.load("promoter_split_model.pth", map_location="cpu"))
model.eval()

# ================= ONE HOT ENCODING =================

def one_hot_encode(seq, max_len=4000):
    mapping = {'A':0, 'C':1, 'G':2, 'T':3}
    encoded = torch.zeros(4, max_len)

    seq = seq.upper()

    for i, char in enumerate(seq[:max_len]):
        if char in mapping:
            encoded[mapping[char], i] = 1.0

    return encoded

# ================= API ROUTE =================

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    promoter = data.get("promoter", "")
    interactor = data.get("interactor", "")

    # ✅ CLEAN INPUT (ADD THIS)
    promoter = promoter.replace("\n", "").replace("\r", "").replace(" ", "")
    interactor = interactor.replace("\n", "").replace("\r", "").replace(" ", "")

    if len(promoter) == 0 or len(interactor) == 0:
        return jsonify({"error": "Both sequences required"}), 400

    promoter_tensor = one_hot_encode(promoter).unsqueeze(0)
    interactor_tensor = one_hot_encode(interactor).unsqueeze(0)

    with torch.no_grad():
        output = model(promoter_tensor, interactor_tensor)
        probability = torch.sigmoid(output).item() * 100

    return jsonify({"probability": round(probability, 2)})

# ================= RUN =================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)