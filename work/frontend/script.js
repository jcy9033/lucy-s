function updateTimestamp() {
  const timestampElement = document.getElementById("timestamp");
  const now = new Date();
  const options = {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  };
  const formattedTimestamp = now.toLocaleString("kr", options);
  timestampElement.textContent = formattedTimestamp;
}

updateTimestamp();

setInterval(updateTimestamp, 60000); // 60000 milliseconds = 1 minute