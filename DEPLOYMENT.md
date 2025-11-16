# Deployment Guide - Tennis Simulator v4.1

## Step-by-Step Instructions to Host Your Simulator Online

### Part 1: Upload to GitHub

1. **Create a GitHub Account** (if you don't have one)
   - Go to https://github.com
   - Click "Sign up"
   - Follow the registration process

2. **Create a New Repository**
   - Click the "+" icon in the top-right corner
   - Select "New repository"
   - Repository name: `tennis-match-simulator` (or any name you prefer)
   - Description: "Tennis Match Monte Carlo Simulator v4.1 - Web-based tennis match simulation"
   - Make it **Public** (required for free Streamlit hosting)
   - ✅ Check "Add a README file"
   - Click "Create repository"

3. **Upload Your Files**
   - Click "uploading an existing file" or "Add file" → "Upload files"
   - Drag and drop these files:
     * `app.py`
     * `tennis_simulator_v41.py`
     * `requirements.txt`
     * `ATP_TOP20_MATCHUPS.txt`
     * `.gitignore`
   - Or replace the README.md with the one provided
   - Click "Commit changes"

### Part 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit https://share.streamlit.io
   - Click "Sign up" or "Sign in"

2. **Sign in with GitHub**
   - Click "Continue with GitHub"
   - Authorize Streamlit to access your GitHub

3. **Deploy Your App**
   - Click "New app" button
   - Select your repository: `your-username/tennis-match-simulator`
   - Branch: `main` (default)
   - Main file path: `app.py`
   - Click "Deploy!"

4. **Wait for Deployment** (1-2 minutes)
   - Streamlit Cloud will install dependencies and launch your app
   - Once complete, you'll get a public URL like:
     `https://your-username-tennis-match-simulator-app-xyz123.streamlit.app`

5. **Share Your App!**
   - Copy the URL
   - Share it with anyone - they can use the simulator without downloading anything
   - Update your GitHub README.md with the live URL

### Part 3: Making Updates (Optional)

If you want to update the app later:

1. **Edit Files on GitHub**
   - Go to your repository
   - Click on the file you want to edit
   - Click the pencil icon (Edit)
   - Make your changes
   - Commit changes

2. **Automatic Redeployment**
   - Streamlit Cloud automatically detects changes
   - Your app will redeploy with the updates
   - Usually takes 1-2 minutes

### Troubleshooting

**Problem: "Module not found" error**
- Solution: Make sure `requirements.txt` is uploaded and contains all dependencies

**Problem: App won't load**
- Solution: Check Streamlit Cloud logs (click "Manage app" → "Logs")
- Common issue: Missing files - make sure all 5 files are uploaded

**Problem: Want to change the URL**
- Solution: Go to Streamlit Cloud → Click your app → Settings → Change app URL

**Problem: App is slow**
- Solution: This is normal for free tier. Consider reducing default simulation count or upgrading to Streamlit Cloud paid tier

### Free Tier Limits

Streamlit Cloud free tier includes:
- ✅ Unlimited public apps
- ✅ 1 GB RAM per app
- ✅ Unlimited viewers
- ⚠️ Apps sleep after inactivity (wake up when someone visits)
- ⚠️ Limited compute resources (may be slow with 1000+ simulations)

### Success!

Once deployed, your simulator will be available at:
`https://your-custom-url.streamlit.app`

Anyone can access it without:
- Installing Python
- Downloading files
- Creating accounts

Just share the link and they can run tennis simulations instantly! 🎾

---

**Need Help?**

- Streamlit Docs: https://docs.streamlit.io
- Streamlit Community: https://discuss.streamlit.io
- GitHub Docs: https://docs.github.com

**Estimated Time:**
- GitHub setup: 5-10 minutes
- Streamlit deployment: 2-5 minutes
- **Total: ~15 minutes** ⚡
