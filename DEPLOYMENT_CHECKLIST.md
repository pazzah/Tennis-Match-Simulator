# ✅ Deployment Checklist - Tennis Simulator v4.1

Use this checklist to deploy your simulator to the web!

## 📋 Pre-Deployment Checklist

- [ ] All 7 files downloaded from Claude
  - [ ] app.py
  - [ ] tennis_simulator_v41.py
  - [ ] requirements.txt
  - [ ] README.md
  - [ ] ATP_TOP20_MATCHUPS.txt
  - [ ] DEPLOYMENT.md
  - [ ] .gitignore

## 🌐 GitHub Setup (5-10 minutes)

- [ ] GitHub account created (or already have one)
- [ ] Logged into GitHub
- [ ] New repository created
  - Repository name: `tennis-match-simulator` (or your choice)
  - Visibility: **Public** (required for free Streamlit)
  - README: Checked ✅
- [ ] All 7 files uploaded to repository
- [ ] Files visible in repository (refresh page to verify)

## ☁️ Streamlit Cloud Setup (5 minutes)

- [ ] Visited https://share.streamlit.io
- [ ] Clicked "Sign up" or "Sign in"
- [ ] Signed in with GitHub account
- [ ] Authorized Streamlit to access GitHub
- [ ] Clicked "New app" button
- [ ] Selected correct repository
- [ ] Main file set to: `app.py`
- [ ] Branch set to: `main`
- [ ] Clicked "Deploy!"
- [ ] Waited for deployment to complete (1-2 minutes)

## 🎉 Post-Deployment

- [ ] App successfully deployed
- [ ] Received public URL (e.g., `https://your-app.streamlit.app`)
- [ ] Tested app by running a simulation
- [ ] Results displayed correctly
- [ ] CSV and Summary downloads work
- [ ] Copied URL for sharing

## 📝 Optional Updates

- [ ] Updated README.md with live app URL
- [ ] Customized app URL in Streamlit settings
- [ ] Shared URL with intended users

## 🔍 Testing Checklist

After deployment, verify these features work:

- [ ] Page loads without errors
- [ ] Player name inputs work
- [ ] All sliders adjust properly
- [ ] All format dropdowns work
- [ ] "Run Simulation" button works
- [ ] Results display correctly
- [ ] Win percentages calculate properly
- [ ] Statistics show up
- [ ] CSV download works
- [ ] Summary download works
- [ ] ATP Top 20 sidebar displays

## ⚠️ Troubleshooting

If something doesn't work:

**App won't load:**
- [ ] Check all files uploaded to GitHub
- [ ] Verify `requirements.txt` is present
- [ ] Check Streamlit Cloud logs (Manage app → Logs)

**Errors during simulation:**
- [ ] Verify `tennis_simulator_v41.py` uploaded correctly
- [ ] Check that file hasn't been renamed

**Missing ATP reference:**
- [ ] Confirm `ATP_TOP20_MATCHUPS.txt` is uploaded

**Deployment failed:**
- [ ] Repository must be Public
- [ ] Main file must be exactly `app.py`
- [ ] Requirements.txt must be valid

## 🎯 Success Criteria

Your deployment is successful when:

✅ App loads at your Streamlit URL
✅ You can run a simulation
✅ Results display correctly
✅ You can download CSV and Summary files
✅ Others can access the URL without logging in

## 📊 Estimated Timeline

- GitHub setup: 5-10 minutes
- Streamlit deployment: 2-5 minutes
- Testing: 2-3 minutes
- **Total: 10-20 minutes**

## 🆘 Still Having Issues?

1. Read DEPLOYMENT.md for detailed instructions
2. Check Streamlit documentation: https://docs.streamlit.io
3. Verify all files are in repository
4. Try redeploying from Streamlit Cloud dashboard

---

**Ready to start?**

1. Check off items as you complete them
2. Follow DEPLOYMENT.md for detailed steps
3. Refer back to this checklist to track progress

**Good luck! 🎾**
