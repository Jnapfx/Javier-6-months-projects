<p align="center">
  <img src="assets/images/javier_headshot.jpeg" alt="Javier Profile" width="300" style="border-radius: 6%;">
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
- [chore: added 4th semester folder with complete project structure](https://github.com/Jnapfx/Javier-6-months-projects/commit/da998e86f4b85704e362a066b73ac8d662f85b71) (da998e8) [2025-08-04]
- [chore: update latest commits section](https://github.com/Jnapfx/Javier-6-months-projects/commit/2fd446f35a7784fa52df1d333a8815c242132386) (2fd446f) [2025-08-04]
- [Test pushing](https://github.com/Jnapfx/Javier-6-months-projects/commit/2018f418be8f0720e33b03e224b708d38980279f) (2018f41) [2025-08-04]
<!-- COMMITS-END -->














---
Take a look around:
- 🐙 [Check out my Github](https://github.com/Jnapfx)  
- 🛠️ [View My Projects](projects.md)  
- 📄 [Download My Resume](assets/files/JAVIER_RESUME.pdf)
- 💼 [Connect on LinkedIn](https://www.linkedin.com/in/javier-napoles-3513031a7)

Thanks for visiting! Let’s connect and grow together. 🚀


<div style="text-align:center; margin-top:2rem;">
  <img src="{{ '/assets/img/dae-logo.jpg' | relative_url }}" alt="DAE Logo" style="height:40px; opacity:0.8;">
</div>








