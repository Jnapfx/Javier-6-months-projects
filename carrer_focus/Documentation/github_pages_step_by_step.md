# 🌐 GitHub Pages Portfolio – Markdown-Only Setup

This guide will help you build a clean, simple portfolio site using **GitHub Pages** and `.md` files only—no HTML or JavaScript required.

---

## 📁 Recommended Folder Structure

```
your-repo/
└── docs/
    ├── index.md
    ├── about.md
    ├── gallery.md
    ├── soc-lab.md
    ├── health-dashboard.md
    ├── assets/
    │   └── Javier-Resume.pdf
    └── _config.yml
```

---

## ✅ Step-by-Step Instructions

### 1️⃣ Create a GitHub Repository
- Name it whatever you want (e.g., `portfolio-site`)
- Add a README if you want
- Clone it locally or use GitHub’s web editor

---

### 2️⃣ Create the `docs/` Folder
GitHub Pages will use this folder as the root of your site.

---

### 3️⃣ Create Your Markdown Pages

#### `docs/index.md`
```markdown
---
title: Home
---

# 👋 Welcome

Hi, I'm [Your Name]! Check out my work:

- [About Me](about.md)
- [Project Gallery](gallery.md)
- [📄 Download My Resume](assets/Javier-Resume.pdf)
```

#### `docs/about.md`
```markdown
---
title: About
---

# 🙋 About Me

I'm a [Your Role] passionate about [your interests].

[← Back to Home](index.md)
```

#### `docs/gallery.md`
```markdown
---
title: Project Gallery
---

# 🚀 Project Gallery

## 📊 Dog Activity Recommender  
Suggests dog activities based on mood and weather.  
- **Tools:** Python, Tkinter  
- [GitHub Repo](https://github.com/yourusername/dog-activity-recommender)

---

## 🔐 SOC Analyst Lab – "Divide & Defend"  
Hands-on SOC simulation with detection, micro-segmentation, and SIEM.  
- **Tools:** VirtualBox, Wazuh, Splunk  
- [Read More](soc-lab.md)

---

## 📈 Healthcare Dashboard  
Dashboard showing patient outcomes using Tableau.  
- **Tools:** SQL, Tableau  
- [Project Page](health-dashboard.md)
```

---

### 4️⃣ Add Individual Project Pages

#### `docs/soc-lab.md`
```markdown
---
title: SOC Analyst Lab
---

# 🔐 SOC Analyst Lab – "Divide & Defend"

This lab simulates a real Security Operations Center environment using threat detection, segmentation, and open-source tools.

[← Back to Projects](gallery.md)
```

#### `docs/health-dashboard.md`
```markdown
---
title: Healthcare Dashboard
---

# 📈 Healthcare Data Dashboard

An interactive dashboard created in Tableau to explore trends in patient recovery data.

[← Back to Projects](gallery.md)
```

---

### 5️⃣ Add a Downloadable Resume

Upload your resume to:  
`docs/assets/Javier-Resume.pdf`

Then link to it in your `.md`:
```markdown
[📄 Download My Resume](assets/Javier-Resume.pdf)
```

---

### 6️⃣ Configure `_config.yml` for Navigation

Create `docs/_config.yml`:

```yaml
title: My Portfolio
remote_theme: pages-themes/slate@v0.2.0
header_pages:
  - index.md
  - about.md
  - gallery.md
```

✅ This activates the top navigation menu.

---

### 7️⃣ Enable GitHub Pages

1. Go to your repo → **Settings** → **Pages**
2. Under **Source**, choose:
   - Branch: `main`
   - Folder: `/docs`
3. Click **Save**

Your site will be published at:
```
https://yourusername.github.io/your-repo-name/
```

---

## 🧠 Final Recap

- ✅ All content in Markdown `.md` files
- 🧭 Top navigation bar
- 📂 Project gallery with descriptions
- 📄 Downloadable resume
- 🌍 Hosted for free via GitHub Pages

---

## 💡 Bonus Tips

- Use `[Link Text](page.md)` for internal links
- You can mix raw HTML in `.md` (e.g., for layout)
- Try other GitHub themes like `minimal`, `cayman`, `architect`


---

### Here you can see all the themes in case you wanna change your actual theme
https://pages.github.com/themes/

### Also you can visit my repository in case you wanna check how I did mine
https://github.com/Jnapfx/Javier-6-months-projects