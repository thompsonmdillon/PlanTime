# PlanTime
A hosted application that allows users to better plan their schedules and manage tasks.


# Developer Notes
Route example of when a user accesses the homepage: User accesses the site and then FastAPI runs the / route. This then returns templates/index.html as seen in the @app.get("/") function, meaning that the HTML loads. Inside index.html, the two lines which reference the style.css and app.js files are read by the browser. The browser then requests those static files. In return, FastAPI then serves them via the mount statement in main.py.