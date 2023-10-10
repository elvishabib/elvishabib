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
                    "Frameworks": ["ExpressJS", "Symfony", "Laravel"],
                    "Databases": ["MySQL", "Redis"],
                    "API Services and Tools": {
                        "Creating APIs": ["ExpressJS", "Laravel"],
                        "Testing APIs": ["Insomnia"]
                    }
                },
                "Frontend": {
                    "JS Libs and Frameworks": ["jQuery", "ReactJS", "Typescript"],
                    "Template Engine": ["HTML5", "Django Template Engine", "Jinja"],
                    "CSS and Frameworks": ["CSS3", "SCSS", "SASS", "TailwindCSS"]
                }
            }
        }

    def say_hi(self):
        print("Welcome, I'm passionate about coding and building cool software projects. Feel free to reach out!")


me = SoftwareDeveloper()
me.say_hi()