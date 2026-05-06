<!DOCTYPE html>
<html>

<head>
  <title>AI Career Planner</title>
</head>

<body>

  <h2>AI Career Planner</h2>

  <input id="goal" placeholder="Enter career goal">
  <button onclick="send()">Generate Plan</button>

  <pre id="output"></pre>

  <script>
    async function send() {

      const goal = document.getElementById("goal").value;

      const res = await fetch(
        `http://127.0.0.1:8000/plan?goal=${goal}`
      );

      const data = await res.json();

      document.getElementById("output").innerText =
        data.career_plan;
    }
  </script>

</body>

</html>