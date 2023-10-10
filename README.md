### Hi there 👋

<!--
**elvishabib/elvishabib** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-


class SoftwareDeveloper:

    def __init__(self):
        self.name = "Elvis Habib Akadjame"
        self.role = "Software Developer"
        self.language_spoken = ["en_US", "fr_FR"]
        self.stack = {
            "Main Stack": {
                "Backend": {
                    "Language": ["Python"],
                    "Frameworks": ["FastAPI", "Django", "Flask"],
                    "Databases": ["MongoDB", "PostgreSQL"],
                    "API Services and Tools": {
                        "Creating APIs": ["FastAPI", "Django Rest", "Flask"],
                        "Testing APIs": ["Postman"]
                    }
                }
            },
            "Side Stack": {
                "Backend": {
                    "Languages": ["JavaScript", "PHP"],
                    "Frameworks": ["Express", "Symfony", "Laravel"],
                    "Databases": ["MySQL", "Redis"],
                    "API Services and Tools": {
                        "Creating APIs": ["Express", "Laravel"],
                        "Testing APIs": ["Insomnia"]
                    }
                },
                "Frontend": {
                    "JS Libs and Frameworks": ["jQuery", "React", "Typescript"],
                    "Template Engine": ["HTML5", "Django Template Engine", "Jinja"],
                    "CSS and Frameworks": ["CSS3", "SCSS", "SASS", "TailwindCSS"]
                }
            }
        }

    def say_hi(self):
        print("Welcome, I'm passionate about coding and building cool software projects. Feel free to reach out!")


me = SoftwareDeveloper()
me.say_hi()
```
