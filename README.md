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
                    },
                    "Operating System": {
                        "Linux": ["Ubuntu Desktop"]
                        "MacOS": []
                    }
                }
            },
            "Side Stack": {
                "Backend": {
                    "Languages": ["JavaScript", "PHP"],
                    "Frameworks": ["ExpressJS", "Symfony", "Laravel"],
                    "Databases": ["MySQL", "Redis"],
                    "API Services and Tools": {
                        "Creating APIs": ["ExpressJS", "Laravel"],
                        "Testing APIs": ["Insomnia"]
                    },
                    "Operating System": {
                        "Windows": []
                    }
                },
                "DevOps & Deployment": {
                    "Webservers and Tools": ["Nginx", "Apache", "Gunicorn", "Docker"],
                    "Cloud Services": {
                        "Digital Ocean": ["Setup and config web apps and APIs for deployment"]
                        "Deta Space": []
                    }
                },
                "Frontend": {
                    "JS Libs and Frameworks": ["jQuery", "React.js (Main)", "Typescript"],
                    "Template Engine": ["HTML5", "Django Template Engine", "Jinja"],
                    "CSS and Frameworks": ["CSS3", "SCSS", "SASS", "TailwindCSS"]
                }
            }
        }

    def say_hi(self):
        self.__init__()
        print(f"Welcome! I'm {self.name}, a {self.role}.")
        print("I'm passionate about coding and building cool software projects.")


    def display_stack(self):
        print("My Current Stack:")
        self.display_stack_recursive(self.stack, 0)

    def display_stack_recursive(self, stack, indent_level):
        indent = "  " * indent_level
        for key, value in stack.items():
            if isinstance(value, dict):
                print(f"{indent}{key}:")
                self.display_stack_recursive(value, indent_level + 1)
            elif isinstance(value, list):
                print(f"{indent}{key}: {', '.join(value)}")
            else:
                print(f"{indent}{key}: {value}")


me = SoftwareDeveloper()
me.say_hi()
me.display_stack()
```
