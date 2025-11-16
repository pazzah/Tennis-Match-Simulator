# Quick Start Guide - Tennis Simulator v4.1 Web Version

## 📦 What You Have

Your tennis simulator has been converted to a web app! Here are the files:

1. **app.py** - Main Streamlit web application
2. **tennis_simulator_v41.py** - Core simulation engine (unchanged)
3. **requirements.txt** - Python package dependencies
4. **README.md** - GitHub repository description
5. **ATP_TOP20_MATCHUPS.txt** - Reference parameters
6. **DEPLOYMENT.md** - Detailed deployment instructions
7. **.gitignore** - Git configuration file

## 🚀 Two Ways to Use Your Simulator

### Option 1: Host Online (Recommended) - FREE! 🌐

**Benefits:**
- ✅ Anyone can use it without downloading
- ✅ No Python installation needed
- ✅ Share a simple URL
- ✅ Access from any device
- ✅ Completely FREE with Streamlit Cloud

**Time Required:** ~15 minutes

**Steps:**
1. Create GitHub account (if needed)
2. Create new repository named `tennis-match-simulator`
3. Upload all 7 files to GitHub
4. Go to https://share.streamlit.io
5. Sign in with GitHub
6. Click "New app"
7. Select your repository
8. Set main file to `app.py`
9. Click "Deploy"
10. Share your URL!

📖 **See DEPLOYMENT.md for detailed step-by-step instructions**

### Option 2: Run Locally on Your Computer 💻

**Benefits:**
- ✅ Works offline
- ✅ Faster performance
- ✅ Full control

**Requirements:**
- Python 3.8 or higher installed

**Steps:**
1. Save all files in one folder
2. Open terminal/command prompt
3. Navigate to folder: `cd path/to/folder`
4. Install dependencies: `pip install -r requirements.txt`
5. Run app: `streamlit run app.py`
6. Browser will open automatically at http://localhost:8501

## 🎯 Key Differences from Original Version

### What Changed:
- ❌ No .bat file needed (web-based now)
- ❌ No command-line prompts (GUI interface)
- ✅ Visual sliders and dropdowns
- ✅ Real-time results display
- ✅ Download buttons for CSV and summary
- ✅ Mobile-friendly interface
- ✅ ATP Top 20 reference in sidebar

### What Stayed the Same:
- ✅ All simulation logic (identical results)
- ✅ All format options (Fast4, Pro Set, etc.)
- ✅ All parameters (serve %, variability, clutch)
- ✅ Head-to-head matchup emphasis
- ✅ Realistic pressure/clutch system
- ✅ Same CSV output structure
- ✅ Same summary statistics

## 📊 Using the Web App

1. **Player Parameters:**
   - Use sliders to set serve %, variability, clutch
   - Reference ATP Top 20 values in sidebar
   - Remember: parameters are matchup-specific!

2. **Format Selection:**
   - Choose match length (1/3/5 sets)
   - Pick set format (Traditional/Fast4/Pro Set/etc.)
   - Select tiebreak type
   - Choose scoring (Advantage/No-Ad)

3. **Run Simulation:**
   - Set number of simulations (100-5000)
   - Click "Run Simulation" button
   - Wait for results (progress bar shown)

4. **View Results:**
   - Win percentages shown as big metrics
   - Average statistics displayed
   - Sample results table at bottom

5. **Download:**
   - Click "Download CSV Results" for full data
   - Click "Download Summary Report" for text summary

## 🎾 Recommended Workflow

### For GitHub/Streamlit Deployment:

1. **Upload files to GitHub:**
   - Go to github.com
   - Create new repository
   - Drag and drop all files

2. **Deploy to Streamlit:**
   - Go to share.streamlit.io
   - Connect to GitHub
   - Select your repo
   - Deploy!

3. **Share your app:**
   - Copy the URL you get
   - Share with anyone
   - They can use immediately!

## 💡 Tips

- **For best results:** Run 500+ simulations
- **For quick tests:** 100 simulations is fine
- **Sharing online:** Free tier may be slow with 1000+ sims
- **Local use:** Can handle 5000+ simulations easily
- **Mobile use:** Web version works great on phones/tablets

## ❓ Common Questions

**Q: Can I still use the old .bat file version?**
A: Yes! Your original v41 files still work. This is just a web version.

**Q: Do I need both versions?**
A: No. Choose whichever you prefer. Web version is easier to share.

**Q: Will Streamlit cost money?**
A: No! Free tier is unlimited for public apps.

**Q: Can I keep the app private?**
A: Free tier requires public GitHub repos. Paid Streamlit plans allow private apps.

**Q: What if I make changes?**
A: Just edit files on GitHub - app auto-updates in 1-2 minutes.

## 🆘 Need Help?

1. **Read DEPLOYMENT.md** - Detailed deployment guide
2. **Read README.md** - Full documentation
3. **Check Streamlit docs:** https://docs.streamlit.io
4. **GitHub help:** https://docs.github.com

## ✅ Next Steps

**Ready to deploy?**
1. Open DEPLOYMENT.md
2. Follow step-by-step instructions
3. Your simulator will be live in ~15 minutes!

**Want to test locally first?**
1. Install Python 3.8+
2. Run: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

---

**🎾 Enjoy your web-based tennis simulator!**

Version 4.1 Web | November 2025
