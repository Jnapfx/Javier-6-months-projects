<p align="center">
  <img src="assets/images/Javier.jpg" alt="Javier Profile" width="300" style="border-radius: 6%;">
</p>

## 👋 Welcome to My Portfolio

Hi there! I'm **Javier**, a creative thinker turned cybersecurity enthusiast with a background in graphic design and threat detection.  
This site showcases the skills, projects, and progress I’ve made in tech and security.


---

## 📝 Latest Commit Posts

{% assign commits = site.data.latest_commits | slice: 0, 5 %}
<ul>
{% for c in commits %}
  <li>
    <a href="{{ c.html_url }}">{{ c.message | split: "\n" | first | escape }}</a>
    — {{ c.author }} on {{ c.date | date: "%b %d, %Y %I:%M %p" }}
  </li>
{% endfor %}
</ul>

<!-- COMMITS-START -->
- [refactor: improved titles on project pages in GitHub Pages](https://github.com/Jnapfx/Javier-6-months-projects/commit/3c45fb13b91da4014a8ae3faa6caf440ff913a4d) (3c45fb1) [2025-07-31]
- [chore: update latest commits section](https://github.com/Jnapfx/Javier-6-months-projects/commit/b8e6cd70e0a084825d7a81d65eb370dc9018bb13) (b8e6cd7) [2025-08-01]
- [fix: repaired broken photo links on project page in GitHub Pages](https://github.com/Jnapfx/Javier-6-months-projects/commit/3ed319ce76b1dbe77fc96620eeb3a9c742b51db2) (3ed319c) [2025-07-31]
- [chore: update latest commits section](https://github.com/Jnapfx/Javier-6-months-projects/commit/cbb789ac2daedbe2f541dbca4c91d1c399ac6610) (cbb789a) [2025-08-01]
- [chore: general improvements on main_project page](https://github.com/Jnapfx/Javier-6-months-projects/commit/8baa0940442fec777688cc37b50b8bfd7af28056) (8baa094) [2025-07-31]
<!-- COMMITS-END -->












---
Take a look around:
- 🐙 [Check out my Github](https://github.com/Jnapfx)  
- 🛠️ [View My Projects](projects.md)  
- 📄 [Download My Resume](assets/files/JAVIER_RESUME.pdf)
- 💼 [Connect on LinkedIn](https://www.linkedin.com/in/javier-napoles-3513031a7)

Thanks for visiting! Let’s connect and grow together. 🚀











