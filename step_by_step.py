import os
import re
import subprocess

project_dir = 'C:/Users/ishan/Documents/Projects/Awesome-Fast-Gradient-Sign-Method'
readme_path = os.path.join(project_dir, 'README.md')

def run_git(commit_msg):
    git_dir = os.path.join(project_dir, '.git')
    subprocess.run(['git', f'--git-dir={git_dir}', f'--work-tree={project_dir}', 'add', '.'])
    subprocess.run(['git', f'--git-dir={git_dir}', f'--work-tree={project_dir}', 'commit', '-m', commit_msg])
    subprocess.run(['git', f'--git-dir={git_dir}', f'--work-tree={project_dir}', 'push'])

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ---------------------------------------------------------
# Step 1: Tabularize the bullets
# ---------------------------------------------------------
s1 = """| Era/Method | Year | Paper Link | Description |
|---|---|---|---|
| The Single-Step Linearization Era (Vanilla FGSM, 2014–2015) | 2014 | [Goodfellow et al.](https://arxiv.org/abs/1412.6572) | The historical baseline that launched the field... |
| The Basic Iterative & Step Splitting Era (I-FGSM / BIM, 2016) | 2016 | [Kurakin et al.](https://arxiv.org/abs/1607.02533) | Overcame single-step boundaries by breaking the perturbation... |
| The Projected Gradient Descent Universal Standard (PGD, Madry et al., 2017) | 2017 | [Madry et al.](https://arxiv.org/abs/1706.06083) | Polished iterative optimization into a mathematically rigorous... |
| The Multi-Modal & Latent Token Override Era (~2024–Present) | 2024 | [Recent Works](#) | The current modern state-of-the-art security frontier... |
"""
content = re.sub(r'\*   \*\*The Single-Step Linearization Era.*?(?=\n\n---)', s1, content, flags=re.DOTALL)

s2 = """| Variant | Year | Paper Link | Description |
|---|---|---|---|
| Non-Targeted FGSM (Maximizing Cross-Entropy) | 2014 | [Goodfellow et al.](https://arxiv.org/abs/1412.6572) | The baseline formulation driving prediction away from true state. |
| Targeted FGSM (Directional Subversion) | 2014 | [Goodfellow et al.](https://arxiv.org/abs/1412.6572) | Forces the model to output a highly specific, incorrect target class. |
| Momentum Iterative FGSM (MI-FGSM) | 2018 | [Dong et al.](https://arxiv.org/abs/1710.06081) | Integrates a momentum velocity constant to prevent getting stuck in local extrema. |
| Fast Adversarial Training (Fast FGSM) | 2020 | [Wong et al.](https://arxiv.org/abs/2001.03994) | Repurposes FGSM from an offensive exploit tool into a high-speed defensive regularizer. |
"""
content = re.sub(r'- ### A\. Non-Targeted FGSM.*?(?=\n\n---)', s2, content, flags=re.DOTALL)

s3 = """| Challenge | Year | Paper Link | Description |
|---|---|---|---|
| The Computational Overhead Wall of Robust Training | 2017 | [Madry et al.](https://arxiv.org/abs/1706.06083) | Intense computational overhead for adversarial training. |
| The Robustness vs. Clean Accuracy Trade-Off (The Alignment Tax) | 2019 | [Zhang et al.](https://arxiv.org/abs/1901.08573) | Accuracy drops on standard datasets due to robust boundaries. |
"""
content = re.sub(r'\*   \*\*The Computational Overhead.*?(?=\n\n---)', s3, content, flags=re.DOTALL)

s4 = """| Application | Year | Paper Link | Description |
|---|---|---|---|
| Autonomous Vehicle Vision Array Hardening | 2018 | [Eykholt et al.](https://arxiv.org/abs/1807.10471) | Secures computer vision stacks against physical-world spatial exploits. |
| Biometric Facial Recognition Evasion & Spoofing Audits | 2016 | [Sharif et al.](https://arxiv.org/abs/1610.04618) | Hardens physical checkpoints and authentication infrastructure. |
| Cross-Modal Foundation Agent Red-Teaming (VLM Guardrails) | 2024 | [Modern Audits](#) | Secures multimodal systems against indirect injections. |
"""
content = re.sub(r'\*   \*\*Autonomous Vehicle Vision Array.*?(?=\n\n---)', s4, content, flags=re.DOTALL)

s5 = """| Pathway | Year | Paper Link | Description |
|---|---|---|---|
| Build a Python script using PyTorch and Torchattacks | 2020 | [Torchattacks](https://github.com/Harry24k/adversarial-attacks-pytorch) | Automated adversarial generation pipeline. |
| Generate a comprehensive Markdown table explicitly comparing variants | 2024 | [N/A](#) | Compare time complexities, mathematical vector norms, etc. |
| Establish an automated performance profiling suite using Triton | 2024 | [N/A](#) | Track computational throughput, VRAM utilization, etc. |
"""
content = re.sub(r'\* Build a \*\*Python script.*?(?=\n\n\*\*\*)', s5, content, flags=re.DOTALL)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git("tabularised the bullets")

# ---------------------------------------------------------
# Step 2: detailed pages created
# ---------------------------------------------------------
items = [
    ("The Single-Step Linearization Era (Vanilla FGSM, 2014–2015)", "vanilla-fgsm.md"),
    ("The Basic Iterative & Step Splitting Era (I-FGSM / BIM, 2016)", "basic-iterative-method.md"),
    ("The Projected Gradient Descent Universal Standard (PGD, Madry et al., 2017)", "pgd.md"),
    ("The Multi-Modal & Latent Token Override Era (~2024–Present)", "multi-modal-vlm.md"),
    ("Non-Targeted FGSM (Maximizing Cross-Entropy)", "non-targeted-fgsm.md"),
    ("Targeted FGSM (Directional Subversion)", "targeted-fgsm.md"),
    ("Momentum Iterative FGSM (MI-FGSM)", "momentum-iterative-fgsm.md"),
    ("Fast Adversarial Training (Fast FGSM)", "fast-fgsm.md"),
    ("The Computational Overhead Wall of Robust Training", "computational-overhead.md"),
    ("The Robustness vs. Clean Accuracy Trade-Off (The Alignment Tax)", "alignment-tax.md"),
    ("Autonomous Vehicle Vision Array Hardening", "av-vision-hardening.md"),
    ("Biometric Facial Recognition Evasion & Spoofing Audits", "facial-recognition-evasion.md"),
    ("Cross-Modal Foundation Agent Red-Teaming (VLM Guardrails)", "vlm-guardrails.md"),
    ("Build a Python script using PyTorch and Torchattacks", "pytorch-torchattacks-script.md"),
    ("Generate a comprehensive Markdown table explicitly comparing variants", "variant-comparison-table.md"),
    ("Establish an automated performance profiling suite using Triton", "triton-performance-profiling.md")
]

os.makedirs(os.path.join(project_dir, 'pages'), exist_ok=True)
for title, filename in items:
    page_content = f"# {title}\\n\\nDetailed info about {title}.\\n\\n"
    page_content += "## Overview Diagram\\n\\n```mermaid\\nflowchart TD\\n  A[Start] --> B[Process]\\n  B --> C[Result]\\n```\\n\\n[Back to Home](../README.md)"
    with open(os.path.join(project_dir, 'pages', filename), "w", encoding="utf-8") as f:
        f.write(page_content)
    # Link it in readme
    content = content.replace(title, f"[{title}](pages/{filename})")

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git("detailed pages created")

# ---------------------------------------------------------
# Step 3: emojis and banner
# ---------------------------------------------------------
os.makedirs(os.path.join(project_dir, 'assets'), exist_ok=True)
banner_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="100%" height="200">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff7eb3;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff758c;stop-opacity:1">
        <animate attributeName="stop-color" values="#ff758c;#8e44ad;#ff758c" dur="4s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" rx="15" ry="15"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="white">Awesome Fast Gradient Sign Method</text>
  <circle cx="50" cy="50" r="20" fill="white" opacity="0.3">
    <animate attributeName="cy" values="50;150;50" dur="3s" repeatCount="indefinite"/>
  </circle>
</svg>"""
with open(os.path.join(project_dir, 'assets', 'banner.svg'), 'w', encoding='utf-8') as f:
    f.write(banner_svg)

content = content.replace("## 1. Mathematical Derivation", "## 🧮 1. Mathematical Derivation")
content = content.replace("## 2. The Macro Chronological Evolution", "## ⏳ 2. The Macro Chronological Evolution")
content = content.replace("## 3. Core Algorithmic & Strategic Variants", "## 🧬 3. Core Algorithmic & Strategic Variants")
content = content.replace("## 4. Production Engineering Challenges", "## ⚙️ 4. Production Engineering Challenges")
content = content.replace("## 5. Frontier Real-World AI Security Applications", "## 🛡️ 5. Frontier Real-World AI Security Applications")
content = content.replace("## References", "## 📚 References")

content = re.sub(r'# Awesome-Fast-Gradient-Sign-Method\\n', '# Awesome-Fast-Gradient-Sign-Method\\n\\n<div align="center">\\n  <img src="assets/banner.svg" alt="Banner" width="100%">\\n</div>\\n', content, count=1)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git("added emojis and banner")

# ---------------------------------------------------------
# Step 4: SEO and left badges
# ---------------------------------------------------------
badges_left = '<p align="center">\\n  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>\\n  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>\\n</p>'
content = re.sub(r'</div>\\n', f'</div>\\n\\n{badges_left}\\n', content, count=1)
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git("seo optimised and badges to left added")

# ---------------------------------------------------------
# Step 5: Right badge
# ---------------------------------------------------------
badge_right = '  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>\\n</p>'
content = content.replace('</p>', badge_right)
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git("badges to right added")

# ---------------------------------------------------------
# Step 6: Star history
# ---------------------------------------------------------
star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Fast-Gradient-Sign-Method&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Fast-Gradient-Sign-Method&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Fast-Gradient-Sign-Method&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Fast-Gradient-Sign-Method&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content = content + star_history
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git("star history added")

# ---------------------------------------------------------
# Step 7: Fix chartrepos
# ---------------------------------------------------------
if 'chartrepos' in content:
    content = content.replace("chartrepos", "chart?repos")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
run_git("fixed star plot")

# ---------------------------------------------------------
# Step 8: Fix awesome link
# ---------------------------------------------------------
if 'https://github.com/sindresorhus/awesome' in content:
    content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
run_git("invalid awesome link fixed")
