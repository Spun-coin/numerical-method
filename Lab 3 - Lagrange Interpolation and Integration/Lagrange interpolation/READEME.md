<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lagrange Interpolation Canvas</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f7f9fa;
            margin: 20px;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }
        canvas {
            border: 1px solid #ddd;
            background-color: #fff;
        }
        .output {
            margin-top: 15px;
            font-size: 1.1rem;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Lagrange Interpolation (HTML5 Canvas)</h2>
    <canvas id="plotCanvas" width="600" height="400"></canvas>
    <div class="output" id="consoleOutput"></div>
</div>

<script>
    // Data points matching the Python script
    const x = [1, 3, 4, 7, 10];
    const y = [-6, 6, 36, 20, 30];
    const xp = 5;
    const n = x.length;

    // Lagrange Interpolation Function
    function lagrange(xArr, yArr, targetX) {
        let yp = 0;
        for (let i = 0; i < n; i++) {
            let mul = 1;
            for (let j = 0; j < n; j++) {
                if (i !== j) {
                    mul *= (targetX - xArr[j]) / (xArr[i] - xArr[j]);
                }
            }
            yp += yArr[i] * mul;
        }
        return yp;
    }

    // Calculate specific target point
    const yp = lagrange(x, y, xp);
    document.getElementById('consoleOutput').innerText = `y(${xp}) = ${yp.toFixed(2)}`;

    // Canvas Setup
    const canvas = document.getElementById('plotCanvas');
    const ctx = canvas.getContext('2d');

    // Plot Padding / Margins
    const padding = { top: 40, right: 40, bottom: 50, left: 60 };
    const width = canvas.width - padding.left - padding.right;
    const height = canvas.height - padding.top - padding.bottom;

    // Axis Limits (With some padding)
    const xMin = 0, xMax = 11;
    const yMin = -15, yMax = 45;

    // Helper functions to map data coordinates to pixel coordinates
    function getXPixel(val) {
        return padding.left + ((val - xMin) / (xMax - xMin)) * width;
    }
    function getYPixel(val) {
        return padding.top + height - ((val - yMin) / (yMax - yMin)) * height;
    }

    // 1. Draw Grid Lines
    ctx.strokeStyle = '#e2e8f0';
    ctx.lineWidth = 1;
    
    // X grid lines
    for (let i = xMin; i <= xMax; i += 1) {
        ctx.beginPath();
        ctx.moveTo(getXPixel(i), padding.top);
        ctx.lineTo(getXPixel(i), padding.top + height);
        ctx.stroke();
    }
    // Y grid lines
    for (let i = -10; i <= yMax; i += 10) {
        ctx.beginPath();
        ctx.moveTo(padding.left, getYPixel(i));
        ctx.lineTo(padding.left + width, getYPixel(i));
        ctx.stroke();
    }

    // 2. Draw Axes Labels & Ticks
    ctx.fillStyle = '#333';
    ctx.font = '12px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';

    // X Ticks
    for (let i = 0; i <= xMax; i += 2) {
        ctx.fillText(i, getXPixel(i), padding.top + height + 8);
    }
    // Y Ticks
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    for (let i = -10; i <= yMax; i += 10) {
        ctx.fillText(i, padding.left - 8, getYPixel(i));
    }

    // Graph Titles & Axis Labels
    ctx.fillStyle = '#000';
    ctx.font = 'bold 14px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText("Lagrange Interpolation", canvas.width / 2, 10); // Title
    
    ctx.font = '13px sans-serif';
    ctx.fillText("x-axis", canvas.width / 2, canvas.height - 20); // X Label
    
    // Y Label (Rotated)
    ctx.save();
    ctx.translate(15, canvas.height / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText("y-axis", 0, 0);
    ctx.restore();

    // 3. Draw Continuous Lagrange Curve (Black Line)
    ctx.beginPath();
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 2;

    const steps = 200;
    for (let i = 0; i <= steps; i++) {
        // Sample evenly from x=1 to x=10
        let currentX = 1 + (9 * i) / steps;
        let currentY = lagrange(x, y, currentX);
        
        if (i === 0) {
            ctx.moveTo(getXPixel(currentX), getYPixel(currentY));
        } else {
            ctx.lineTo(getXPixel(currentX), getYPixel(currentY));
        }
    }
    ctx.stroke();

    // 4. Draw Original Data Points (Green Circles)
    ctx.fillStyle = 'green';
    for (let i = 0; i < n; i++) {
        ctx.beginPath();
        ctx.arc(getXPixel(x[i]), getYPixel(y[i]), 5, 0, 2 * Math.PI);
        ctx.fill();
    }

    // 5. Draw Interpolated Point (Red 'X')
    const xPoint = getXPixel(xp);
    const yPoint = getYPixel(yp);
    const size = 6;

    ctx.strokeStyle = 'red';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    // Diagonal line 1
    ctx.moveTo(xPoint - size, yPoint - size);
    ctx.lineTo(xPoint + size, yPoint + size);
    // Diagonal line 2
    ctx.moveTo(xPoint + size, yPoint - size);
    ctx.lineTo(xPoint - size, yPoint + size);
    ctx.stroke();

    // 6. Draw Legend box
    const legX = padding.left + 15;
    const legY = padding.top + 15;
    ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
    ctx.strokeStyle = '#ccc';
    ctx.lineWidth = 1;
    ctx.fillRect(legX, legY, 110, 35);
    ctx.strokeRect(legX, legY, 110, 35);

    // Legend Text & Marker
    ctx.strokeStyle = 'red';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(legX + 10 - 4, legY + 18 - 4); ctx.lineTo(legX + 10 + 4, legY + 18 + 4);
    ctx.moveTo(legX + 10 + 4, legY + 18 - 4); ctx.lineTo(legX + 10 - 4, legY + 18 + 4);
    ctx.stroke();

    ctx.fillStyle = '#000';
    ctx.font = '12px sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'middle';
    ctx.fillText("Interpolated", legX + 22, legY + 18);

</script>

</body>
</html>
