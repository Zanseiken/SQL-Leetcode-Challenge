# Step-by-Step Usage Guide

## For First-Time Users

### Step 1: Install Dependencies (1 minute)
```bash
cd /path/to/SQL-Leetcode-Challenge
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed requests-2.31.0
```

### Step 2: (Optional) Set Up GitHub Token (2 minutes)

Without a token, you get 60 API requests per hour. With a token, you get 5000.

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: "VLA Repo Finder"
4. Select scope: `public_repo` (just this one is enough)
5. Click "Generate token"
6. Copy the token (you'll only see it once!)
7. Set it as environment variable:

```bash
# Linux/Mac
export GITHUB_TOKEN='ghp_your_token_here'

# Windows (PowerShell)
$env:GITHUB_TOKEN='ghp_your_token_here'

# Windows (CMD)
set GITHUB_TOKEN=ghp_your_token_here
```

### Step 3: Run the Tool (2 minutes)
```bash
python3 github_repo_finder.py
```

**What happens:**
- Searches 14 different queries on GitHub
- Filters repos with < 100 stars
- Scores them by relevance
- Creates two files:
  - `VLA_GitHub_Repos.md` (human-readable)
  - `vla_repos.json` (machine-readable)

**Expected output:**
```
================================================================================
GitHub Repository Finder for VLA AI Engineer Role
================================================================================
...
✓ Results saved to VLA_GitHub_Repos.md
✓ Results exported to vla_repos.json
================================================================================
```

### Step 4: Review Results (5-10 minutes)
```bash
# View the results
cat VLA_GitHub_Repos.md

# Or open in your favorite editor
code VLA_GitHub_Repos.md
nano VLA_GitHub_Repos.md
```

**Look for:**
- Repository name and stars
- Description
- Programming language
- Topics/tags
- Relevance score

### Step 5: Select Repositories to Use (10 minutes)

Choose 2-3 repositories based on:
1. **Interest** - Does the topic excite you?
2. **Complexity** - Can you understand the code?
3. **Activity** - Is it recently updated?
4. **Opportunity** - Are there open issues you could fix?

**Mark your selections:**
```bash
# Star the repos on GitHub
# Fork them to your account
# Clone them locally
```

## Quick Actions

### If You're in a Hurry

**Option A: No API Access**
```bash
# Just read the examples
cat EXAMPLE_REPOS.md
# Pick 2-3 repos and search for them manually on GitHub
```

**Option B: With API Access (10 minutes total)**
```bash
# 1. Install (1 min)
pip install -r requirements.txt

# 2. Run (2 min)
python3 github_repo_finder.py

# 3. Review top 10 (5 min)
head -50 VLA_GitHub_Repos.md

# 4. Pick 2-3 repos (2 min)
# Note down their URLs
```

## For Job Application

### Timeline: 1 Week Before Applying

**Day 1-2: Research (2-4 hours)**
- Run the tool
- Review results
- Pick 3 repositories
- Read their README files
- Understand what they do

**Day 3-4: Hands-On (4-6 hours)**
- Clone the repositories
- Set up development environment
- Run the code
- Try the examples
- Identify potential improvements

**Day 5-6: Contribute (4-8 hours)**
- Fix a typo or improve documentation (easiest)
- Add a test case (medium)
- Fix a bug (harder)
- Add a feature (hardest)

**Day 7: Update CV (1-2 hours)**
- Add projects to CV
- Prepare talking points
- Practice explaining your work

### Immediate Action (Before Applying Today)

If you need to apply NOW:

1. **Read EXAMPLE_REPOS.md** (5 min)
2. **Pick 2-3 example repos** (2 min)
3. **Search for similar real repos on GitHub** (5 min)
4. **Star and fork them** (1 min)
5. **Add to CV** (10 min):

```
RELEVANT PROJECTS & INTERESTS
• Exploring Vision-Language-Action models for robotic control
  - Studying RT-2, OpenVLA implementations
  - GitHub: github.com/yourusername (starred/forked relevant projects)
  
• Experience with multimodal AI frameworks
  - Familiar with LLaVA, BLIP-2, CLIP architectures
  - Interest in embodied AI and human-robot interaction
```

## Troubleshooting

### "Rate limit exceeded"
**Solution:**
- Wait 1 hour, OR
- Set GITHUB_TOKEN (see Step 2), OR
- Use EXAMPLE_REPOS.md

### "No repositories found"
**Solution:**
- Check internet connection
- Verify GitHub is accessible
- Try with GITHUB_TOKEN
- Use EXAMPLE_REPOS.md as backup

### "Module not found: requests"
**Solution:**
```bash
pip install requests
```

### Can't run Python script
**Solution:**
```bash
# Try python instead of python3
python github_repo_finder.py

# Or install Python 3
sudo apt install python3  # Linux
brew install python3       # Mac
# Download from python.org (Windows)
```

## Getting Help

### Documentation Files
- **QUICKSTART.md** - Quick start guide
- **VLA_JOB_SEARCH_README.md** - Full documentation  
- **EXAMPLE_REPOS.md** - Example repositories
- **SUMMARY.md** - Technical summary
- **This file** - Step-by-step instructions

### Common Questions

**Q: How many repositories should I include in my CV?**
A: 2-3 with specific contributions > 10 without context

**Q: What if I can't run the code?**
A: Start with documentation improvements or code review

**Q: Should I contribute before applying?**
A: Ideal, but not required. At minimum: star, fork, and understand the repos

**Q: What if repositories are old/unmaintained?**
A: That's okay! Fork them and revive them - shows initiative

## Success Checklist

Before submitting your job application:

- [ ] Tool executed successfully OR reviewed EXAMPLE_REPOS.md
- [ ] Found 10+ relevant repositories
- [ ] Selected 2-3 to focus on
- [ ] Starred and forked selected repos
- [ ] Read README and understood what they do
- [ ] Updated CV with projects
- [ ] Prepared 2-3 talking points per project
- [ ] Can explain why you chose these repos
- [ ] Can discuss what you learned
- [ ] Ready to talk about potential improvements

## Next Steps After Using This Tool

1. **Review your results** - Look at what was found
2. **Pick your favorites** - 2-3 repositories max
3. **Deep dive** - Really understand them
4. **Contribute** - Even small improvements count
5. **Document** - Keep notes on what you learned
6. **Update CV** - Add specific examples
7. **Practice** - Prepare to discuss in interview
8. **Apply** - Submit your application!

## Tips for Success

✅ **Do:**
- Focus on quality over quantity
- Actually understand the code
- Make meaningful contributions
- Be honest about your experience level
- Show enthusiasm for learning

❌ **Don't:**
- List repos you haven't looked at
- Claim work you didn't do
- Copy code without understanding
- Submit spam pull requests
- Exaggerate your contributions

## Good Luck!

You now have everything you need to find relevant repositories and boost your CV for VLA AI Engineer positions. 

**Remember:** The goal isn't to become an expert overnight, but to show genuine interest, learning ability, and hands-on engagement with relevant technologies.

🚀 **You've got this!**
