from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(title="Czech Republic History", description="A flashy pink app about Czech history")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Czech Republic History</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap');
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Comic Neue', cursive;
                background: linear-gradient(45deg, #ff69b4, #ff1493, #ffc0cb, #ff69b4);
                background-size: 400% 400%;
                animation: gradientShift 3s ease infinite;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                overflow-x: hidden;
            }
            
            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            .container {
                background: rgba(255, 255, 255, 0.9);
                border-radius: 30px;
                padding: 40px;
                margin: 20px;
                box-shadow: 0 20px 40px rgba(255, 20, 147, 0.3);
                border: 5px solid #ff1493;
                max-width: 800px;
                text-align: center;
                position: relative;
                overflow: hidden;
            }
            
            .container::before {
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: linear-gradient(45deg, transparent, rgba(255, 182, 193, 0.3), transparent);
                animation: shimmer 2s linear infinite;
            }
            
            @keyframes shimmer {
                0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
                100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
            }
            
            h1 {
                color: #ff1493;
                font-size: 3.5em;
                margin-bottom: 30px;
                text-shadow: 3px 3px 0px #ff69b4, 6px 6px 0px #ffc0cb;
                animation: bounce 2s infinite;
                position: relative;
                z-index: 1;
            }
            
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                40% { transform: translateY(-20px); }
                60% { transform: translateY(-10px); }
            }
            
            .history-text {
                font-size: 1.3em;
                line-height: 1.8;
                color: #333;
                background: linear-gradient(135deg, #ff69b4, #ff1493);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                position: relative;
                z-index: 1;
                text-align: justify;
                margin: 20px 0;
            }
            
            .sparkle {
                position: absolute;
                width: 10px;
                height: 10px;
                background: #ffd700;
                border-radius: 50%;
                animation: sparkle 1.5s linear infinite;
            }
            
            @keyframes sparkle {
                0% { opacity: 0; transform: scale(0); }
                50% { opacity: 1; transform: scale(1); }
                100% { opacity: 0; transform: scale(0); }
            }
            
            .sparkle:nth-child(1) { top: 20%; left: 10%; animation-delay: 0s; }
            .sparkle:nth-child(2) { top: 30%; right: 15%; animation-delay: 0.3s; }
            .sparkle:nth-child(3) { bottom: 25%; left: 20%; animation-delay: 0.6s; }
            .sparkle:nth-child(4) { bottom: 35%; right: 10%; animation-delay: 0.9s; }
            .sparkle:nth-child(5) { top: 50%; left: 5%; animation-delay: 1.2s; }
            .sparkle:nth-child(6) { top: 60%; right: 5%; animation-delay: 1.5s; }
            
            .footer {
                margin-top: 30px;
                color: #ff1493;
                font-size: 1.1em;
                font-weight: bold;
                text-shadow: 2px 2px 0px #ffc0cb;
                position: relative;
                z-index: 1;
            }
            
            .pulse {
                animation: pulse 1.5s ease-in-out infinite;
            }
            
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
        </style>
    </head>
    <body>
        <div class="container pulse">
            <div class="sparkle"></div>
            <div class="sparkle"></div>
            <div class="sparkle"></div>
            <div class="sparkle"></div>
            <div class="sparkle"></div>
            <div class="sparkle"></div>
            
            <h1>🇨🇿 Czech Republic History 🇨🇿</h1>
            
            <div class="history-text">
                The Czech Republic, nestled in the heart of Central Europe, boasts a rich and tumultuous history spanning over a millennium, beginning with the legendary founding of Prague by Princess Libuše in the 8th century and the establishment of the Great Moravian Empire in the 9th century, which became the first Slavic state to adopt Christianity under Saints Cyril and Methodius. The medieval Kingdom of Bohemia, ruled by the Přemyslid dynasty and later the powerful Luxembourg dynasty, reached its golden age under Charles IV (1346-1378), who made Prague the capital of the Holy Roman Empire and founded Charles University, the oldest university in Central Europe. The 15th century Hussite Wars, led by Jan Hus and his followers, marked the first major Protestant reformation in Europe, challenging the Catholic Church's authority and establishing Czech religious independence. After centuries of Habsburg rule following the Battle of White Mountain in 1620, the Czech lands experienced the Czech National Revival in the 19th century, culminating in the creation of Czechoslovakia in 1918 under the leadership of Tomáš Garrigue Masaryk, which became one of the most prosperous democracies in interwar Europe. The dark period of Nazi occupation during World War II and the subsequent communist rule from 1948 to 1989, including the Prague Spring of 1968 and its brutal suppression, was finally ended by the Velvet Revolution in 1989, led by Václav Havel, resulting in the peaceful dissolution of Czechoslovakia and the birth of the independent Czech Republic in 1993, which has since become a thriving democratic nation and proud member of the European Union, NATO, and the Visegrád Group.
            </div>
            
            <div class="footer">
                ✨ Made with 💖 and lots of pink sparkles! ✨
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Czech Republic History API is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
