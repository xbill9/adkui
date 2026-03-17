import os
import sys

# Add Agent3/tools to path so we can import file_writer
sys.path.append(os.path.join(os.getcwd(), "Agent3", "tools"))
from file_writer import write_comic_html

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Story of Momotaro - Comic</title>
    <style>
        body {
            background-color: #1a1a1a;
            color: #f0f0f0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        h1 {
            color: #ffcc00;
            text-shadow: 2px 2px 4px #000;
        }
        .comic-container {
            max-width: 800px;
            width: 100%;
        }
        .panel {
            background-color: #333;
            border: 4px solid #555;
            border-radius: 8px;
            margin-bottom: 40px;
            overflow: hidden;
            box-shadow: 0 10px 20px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
        }
        .panel:hover {
            transform: scale(1.02);
        }
        .panel img {
            width: 100%;
            height: auto;
            display: block;
        }
        .panel-content {
            padding: 20px;
        }
        .narrator {
            font-style: italic;
            color: #ff99cc;
            margin-bottom: 10px;
        }
        .dialogue {
            font-weight: bold;
        }
        .character-name {
            color: #00ffcc;
            text-transform: uppercase;
        }
        @media (max-width: 600px) {
            body { padding: 10px; }
            .panel { margin-bottom: 20px; }
        }
    </style>
</head>
<body>
    <h1>The Story of Momotaro</h1>
    <div class="comic-container">
        <div class="panel">
            <img src="images/panel_1.png" alt="Panel 1">
            <div class="panel-content">
                <div class="narrator">NARRATOR: Long, long ago, in a peaceful village, lived a kind but sorrowful elderly couple. Their greatest wish remained unfulfilled: a child to call their own. One morning, by the river...</div>
            </div>
        </div>
        <div class="panel">
            <img src="images/panel_2.png" alt="Panel 2">
            <div class="panel-content">
                <div class="dialogue"><span class="character-name">MOMOTARO (BABY):</span> Don't be afraid. The Heavens have sent me to be your son.</div>
            </div>
        </div>
        <div class="panel">
            <img src="images/panel_3.png" alt="Panel 3">
            <div class="panel-content">
                <div class="dialogue"><span class="character-name">MOMOTARO:</span> I must go to Onigashima. I will defeat the Oni and reclaim what they have stolen. Our people cannot live in fear any longer.</div>
                <div class="dialogue"><span class="character-name">OLD WOMAN:</span> My son... Onigashima is a den of demons! It is too dangerous!</div>
            </div>
        </div>
        <div class="panel">
            <img src="images/panel_4.png" alt="Panel 4">
            <div class="panel-content">
                <div class="dialogue"><span class="character-name">MOMOTARO:</span> Greetings, noble dog. I am Momotaro, on a quest to defeat the Oni. Are you hungry?</div>
                <div class="dialogue"><span class="character-name">SPOTTED DOG:</span> Such strength! Such flavor! My loyalty is yours, master Momotaro! I shall follow you!</div>
            </div>
        </div>
        <div class="panel">
            <img src="images/panel_5.png" alt="Panel 5">
            <div class="panel-content">
                <div class="narrator">NARRATOR: With his allies gathered, Momotaro taught them that despite their differences, unity was their greatest strength. Together, they journeyed towards the sea, their resolve unwavering.</div>
            </div>
        </div>
        <div class="panel">
            <img src="images/panel_6.png" alt="Panel 6">
            <div class="panel-content">
                <div class="dialogue"><span class="character-name">MOMOTARO:</span> FOR THE VILLAGE! FOR JUSTICE!</div>
                <div class="dialogue"><span class="character-name">SPOTTED DOG:</span> WOOF! You demons are finished!</div>
            </div>
        </div>
        <div class="panel">
            <img src="images/panel_7.png" alt="Panel 7">
            <div class="panel-content">
                <div class="dialogue"><span class="character-name">KING OF THE ONI:</span> NO! Impossible! You... you defeated me, Momotaro! Have mercy! I beg you!</div>
                <div class="dialogue"><span class="character-name">MOMOTARO:</span> Your reign of terror is over, King.</div>
            </div>
        </div>
        <div class="panel">
            <img src="images/panel_8.png" alt="Panel 8">
            <div class="panel-content">
                <div class="dialogue"><span class="character-name">VILLAGER 5:</span> Momotaro has returned! And he defeated the Oni!</div>
                <div class="narrator">NARRATOR: The legend of Momotaro, the Peach Boy, lives on.</div>
            </div>
        </div>
    </div>
</body>
</html>
"""

result = write_comic_html(html_content, "images")
print(result)
