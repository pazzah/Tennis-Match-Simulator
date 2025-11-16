# 🎾 Tennis Match Monte Carlo Simulator v4.1

A comprehensive web-based tennis match simulator with realistic pressure and clutch modeling. Simulate professional tennis matches with head-to-head matchup parameters and advanced statistical analysis.

**[Try it live here!](#)** *(Add your Streamlit Cloud URL after deployment)*

![Tennis Simulator](https://img.shields.io/badge/version-4.1-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Features

- **Head-to-Head Matchup Parameters**: Model specific player matchups, not general abilities
- **Realistic Pressure System**: Hierarchical pressure weighting for break points and game situations
- **Non-linear Clutch Modeling**: Validated against Top 20 ATP/WTA performance
- **Complete Format Flexibility**:
  - Traditional sets, Fast4, Pro Sets, Short Sets
  - All tiebreak variants (5pt, 7pt, 10pt, 12pt)
  - Best of 1, 3, or 5 sets
  - Advantage or No-Ad scoring
- **Comprehensive Statistics**: 50+ data points per match
- **ATP Top 20 Reference Parameters**: Pre-configured matchup data

## 🎯 Key Concept

**CRITICAL**: Parameters reflect THIS SPECIFIC MATCHUP, not general player ability.

Example:
- Kyrgios vs #100 player → Serve 72% (dominant)
- Kyrgios vs Djokovic → Serve 63% (much harder)

## 🚀 Quick Start

### Online (Recommended)

Just visit the live app - no installation required!

**[Launch Simulator](#)** *(Add your Streamlit Cloud URL)*

### Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/tennis-simulator.git
cd tennis-simulator

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📊 Parameters Guide

### Serve Win % (0-100)
How often a player wins serve points **in this specific matchup**:
- 55-60%: Weak matchup
- 60-64%: Below average
- 64-67%: Average
- 67-70%: Strong
- 70%+: Dominant

### Serve Variability (1-8%)
Point-to-point consistency:
- 2-3%: Very consistent (Djokovic, Medvedev)
- 3-4%: Consistent (Sinner)
- 4-5%: Normal variance (Alcaraz)
- 5-6%: Erratic (Rune)

### Clutch Factor (-5 to +5)
Performance on pressure points:
- +4/+5: Elite (Djokovic)
- +2/+3: Excellent (Alcaraz, Sinner)
- 0/+1: Neutral to Good
- -1/-2: Weakness under pressure
- -3/-5: Significant choke tendency

## 🎾 Example Matchups (ATP Top 20)

### Sinner vs Alcaraz
- **Sinner**: 64% serve, 3.5% var, +2 clutch
- **Alcaraz**: 63% serve, 4.5% var, +3 clutch

### Djokovic vs Alcaraz  
- **Djokovic**: 63% serve, 3.0% var, +4 clutch
- **Alcaraz**: 63% serve, 4.5% var, +3 clutch

### Sinner vs Djokovic
- **Sinner**: 62% serve, 3.5% var, +2 clutch
- **Djokovic**: 63% serve, 3.0% var, +4 clutch

See `ATP_TOP20_MATCHUPS.txt` for complete parameter tables.

## 📈 Output

The simulator provides:

1. **Win Percentages**: Match outcome probabilities
2. **Average Statistics**: Games, points, break points per match
3. **Player-Specific Stats**: Serve percentages, break point conversion
4. **Downloadable Results**:
   - CSV file with all match data (50+ columns)
   - Summary report with detailed analysis

## 🔧 Match Format Options

### Set Formats
- Traditional (to 6 games)
- Fast4 (to 4 games)
- Pro Set (to 8 games)
- Short Sets (from 0-0 or 2-2)

### Tiebreak Formats
- Slam (7pt regular, 10pt final)
- 5 points all sets (Fast4)
- 10 points all sets
- 12 points all sets (Pro Set)

### Match Lengths
- Single Set
- Best of 3 Sets
- Best of 5 Sets

## 📚 Files

- `app.py`: Streamlit web interface
- `tennis_simulator_v41.py`: Core simulation engine
- `ATP_TOP20_MATCHUPS.txt`: Reference parameters
- `requirements.txt`: Python dependencies

## 🎓 How to Use

1. **Enter Player Names**: Name your matchup
2. **Set Parameters**: Use ATP Top 20 reference or custom values
3. **Choose Format**: Select set type, tiebreak, scoring
4. **Run Simulation**: Choose number of iterations (500+ recommended)
5. **Analyze Results**: View statistics and download data

## 💡 Tips

- ✅ Use matchup-specific parameters, not general abilities
- ✅ Start with ATP Top 20 reference values
- ✅ Run 500+ simulations for reliable results
- ✅ Validate against actual head-to-head records
- ✅ Adjust for current form and surface conditions

## 🔬 Pressure System

The simulator uses realistic pressure weighting:

**Highest Pressure Situations:**
1. Down 3 breaks (8.5 pressure)
2. Down 2 breaks (6.0 pressure)
3. Triple break point 0-40 (+5.0)
4. Double break point 15-40 (+4.5)
5. Break point 30-40 (+4.0)

**Clutch Impact:**
- Non-linear scaling (square root)
- Maximum ±5% serve win swing at highest pressure
- Validated vs Top 20 ATP/WTA performance

## 🤝 Contributing

Contributions welcome! Please feel free to submit pull requests or open issues.

## 📄 License

MIT License - feel free to use and modify for your projects.

## 🙏 Acknowledgments

Built with:
- Python 3.8+
- Streamlit
- NumPy & Pandas

---

**Version 4.1** | November 2025

For questions or feedback, please open an issue on GitHub.

🎾 **Enjoy realistic tennis match simulation!** 🎾
