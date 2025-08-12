


<div style="display:flex; gap:20px; align-items:center; flex-wrap:wrap; margin-bottom:2rem; padding:1.5rem; background:#f8f9fa; border-radius:8px;">
  <img src="{{ 'assets/images/javier_headshot.jpeg' | relative_url }}" alt="Headshot of Javier Napoles" 
       style="max-width:160px; border-radius:50%; box-shadow:0 4px 12px rgba(0,0,0,.15);">
  <div>
    <h1 style="margin:0; color:#2c3e50;">Javier Napoles</h1>
    <p style="margin:.5rem 0; font-size:1.1rem; color:#34495e;">Cybersecurity Student · Graduating Oct 2025</p>
    <p style="margin:.5rem 0; line-height:1.6;"> Hi there! I’m **Javier** — a creative thinker turned cybersecurity enthusiast, blending a background in graphic design with hands-on experience in threat detection. My journey combines a sharp eye for detail from the design world with a passion for securing enterprise environments through SOC analysis and blue-team operations. I build labs, tune detections, and document repeatable security playbooks, showcasing my skills, projects, and progress as I grow in tech and security.</p>
  </div>
</div>


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





<div style="display:flex; gap:20px; align-items:center; flex-wrap:wrap; margin-bottom:2rem; padding:1.5rem; background:#f8f9fa; border-radius:8px;">
 
  <div>
    - 🐙 [Check out my Github](https://github.com/Jnapfx)
    - 🛠️ [View My Projects](projects.md)
    - 📄 [Download My Resume](assets/files/JAVIER_RESUME.pdf)
    - 💼 [Connect on LinkedIn](https://www.linkedin.com/in/javier-napoles-3513031a7)
  </div>
</div>

---
Take a look around:
- 🐙 [Check out my Github](https://github.com/Jnapfx)  
- 🛠️ [View My Projects](projects.md)  
- 📄 [Download My Resume](assets/files/JAVIER_RESUME.pdf)
- 💼 [Connect on LinkedIn](https://www.linkedin.com/in/javier-napoles-3513031a7)

Thanks for visiting! Let’s connect and grow together. 🚀


<div style="text-align:left; margin-top:2rem;">
  <img src="{{ '/assets/img/dae_logo.png' | relative_url }}" alt="DAE Logo" style="height:40px; opacity:0.8;">
</div>








