# 🧠 Beam-Column Strength Predictor (CFS)

This web-based application predicts the normalized axial strength (P/Py) of cold-formed steel (CFS) beam-column elements using a deep learning model developed in TensorFlow.

🔗 **Live App**: [https://your-app-name.onrender.com](https://your-app-name.onrender.com)  
📂 **Source Code**: [https://github.com/yourusername/beam-column-strength-app](https://github.com/yourusername/beam-column-strength-app)

---

## 📥 Inputs

| Parameter     | Description                                      |
|---------------|--------------------------------------------------|
| `h/t`         | Web slenderness ratio                            |
| `b/t`         | Flange slenderness ratio                         |
| `c/t`         | Lip slenderness ratio                            |
| `kL/ry`       | Column slenderness ratio                         |
| `λ<sub>C</sub>/λ<sub>F</sub>` | Compression-to-flexural slenderness ratio        |
| `Ex (mm)`     | Effective length in x-direction (mm)             |
| `Ey (mm)`     | Effective length in y-direction (mm)             |
| `rx/ry`       | Radius of gyration ratio                         |

---

## 🚀 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/beam-column-strength-app.git
   cd beam-column-strength-app
   ```

2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📦 Files

- `app.py`: Flask app backend
- `templates/index.html`: Web form UI
- `beam_column_model.keras`: Pre-trained Keras DL model
- `scaler.pkl`: Scikit-learn scaler for input normalization

---

## 📜 Citation

If you use this app or model in your research, please cite:

> Mojtabaei, M. (2025). *Beam-Column Strength Predictor for Cold-Formed Steel Elements*.  
> Available at: [https://your-app-name.onrender.com](https://your-app-name.onrender.com)

---

## 📖 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
