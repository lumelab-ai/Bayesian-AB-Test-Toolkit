![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-854FF5?style=for-the-badge&logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-14637D?style=for-the-badge&logo=seaborn&logoColor=white)
![ipywidgets](https://img.shields.io/badge/ipywidgets-FFB000?style=for-the-badge&logo=jupyter&logoColor=white)

# Bayesian Bayesian A/B Test 📊

**Bayesian Bayesian A/B Test** is a self-contained, interactive toolkit designed to help Product Managers, Growth Hackers, and Business Analysts analyze A/B tests with zero coding required. 

Instead of dealing with confusing p-values and frequentist statistics, this toolkit centers decision-making around direct business questions: **"Which variant is more likely to be the best?"** and **"What is the financial/conversion risk of deploying it?"**

---

## 🚀 Two Ways to Run the Toolkit

Choose the option that fits your workflow best. Both interfaces are fully interactive.

### Option A: Google Colab (Zero Setup - Recommended)
Run the toolkit in the cloud in under 60 seconds with no local installation.

1. **Open the Notebook in Colab:**
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1GwC2Z1jYcdkw-ci1Mdy3EVkmptg8uH5-?usp=sharing)
2. **Run All Cells:** Go to `Runtime` -> `Run all` (or press `Ctrl + F9` / `Cmd + F9`).
3. **Upload & Configure:** When prompted in the **Control Panel**, upload your Excel data file. Adjust the sliders for prior selection and risk tolerance, and the report will generate automatically.

---

### Option B: Local Jupyter Notebook
If you prefer to run the analysis locally on your machine.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lumelab-ai/Bayesian-AB-Test-Toolkit.git
   cd Bayesian-AB-Test-Toolkit
   ```
2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch Jupyter Lab:**
   ```bash
   jupyter lab "Bayesian A-B Test - Notebook.ipynb"
   ```
4. **Run the Notebook:** Execute the cells from top to bottom. Use the **Control Panel** in the interface to upload your data and adjust settings.

---

## 📊 How to Prepare Your Data

Your A/B test data must be in an Excel file (`.xlsx`) with the columns `variant`, `reach`, and `conversion`. 

An example template is available at `examples/data_ab.xlsx`.

| variant | reach  | conversion |
| ------- | ------ | ---------- |
| A       | 10000  | 950        |
| B       | 10050  | 1020       |
| C       | 9980   | 965        |

*   **`variant`**: The label of your test groups (e.g., A, B, C, D).
*   **`reach`**: The total number of users who saw the variant (e.g., messages delivered, page views).
*   **`conversion`**: The number of successful conversion actions (e.g., purchases, clicks, sign-ups).

---

## 🎛️ Understanding the Interactive Outputs

Once you upload your data, the toolkit generates three rich interactive sections:

### 1. The Control Panel
A simple, interactive dashboard widget:
*   **Prior Selection**: Select how to treat historical baseline data (Uniform/Non-informative for brand new tests, or Informed/Beta priors to incorporate previous campaign baseline conversion rates).
*   **Risk Tolerance Slider**: Define the maximum conversion loss your business is willing to tolerate (e.g., maximum 1% risk).

### 2. Ridgeline Posterior Distributions (Visual comparison)
An automated, color-coded density plot showing the probability distribution of the conversion rate for each variant. 
*   Includes shaded **95% Credible Intervals** (Bayesian counterpart to confidence intervals) so you can visually assess the uncertainty and overlap between variants.

### 3. Automated Executive Report (Plain English)
Generates a formatted markdown report designed to be copied directly into stakeholder presentations:
*   **Clear Verdict**: Absolute recommendation of which variant to deploy (or whether the test needs to keep running).
*   **Stakeholder Summary**: Highlights the winning probability and quantifies the expected conversion uplift.
*   **Risk Evaluation**: Explains the exact business risk (Expected Loss) of choosing the suggested winner.

---

## 💡 Why Bayesian A/B Testing for Business?

Traditional A/B testing relies on *p-values*, answering a counter-intuitive question: *“Is this data surprising if both variants are exactly identical?”* This makes it easy to stop tests too early or misinterpret results.

The **Bayesian Bayesian A/B Test** toolkit directly answers the business questions that matter:
1.  **What is the probability that Variant B is better than Variant A?** (e.g., *"Variant B has a 92% probability of being the best format"*).
2.  **If I deploy the winning variant, how much do I stand to lose if the decision is wrong?** (*Expected Loss* tells you: *"If B is secretly worse, you stand to lose at most 0.15% in conversion rate"*).
3.  **Is the decision safe?** If the expected loss is lower than your risk threshold, you can safely deploy immediately without waiting for a fixed sample size.

---

## 📄 License

Distributed under the **GNU General Public License v3.0**. See the `LICENSE` file for full details.
