document.addEventListener("DOMContentLoaded", () => {
  const widget = document.createElement("div");
  widget.innerHTML = `
    <div id="chat-widget">
      <button id="chat-toggle">🧑‍🍳</button>
      <div id="chat-box">
        <div id="chat-messages"></div>
        <div id="chat-input">
          <input type="text" id="userInput" placeholder="Ask about recipes...">
          <button id="sendBtn">➤</button>
        </div>
      </div>
    </div>
  `;
  document.body.appendChild(widget);

  const chatBox = document.getElementById("chat-box");
  const toggleBtn = document.getElementById("chat-toggle");
  const input = document.getElementById("userInput");
  const sendBtn = document.getElementById("sendBtn");
  const msgBox = document.getElementById("chat-messages");

  // Load chat state from localStorage
  if (localStorage.getItem("chatOpen") === "true") {
    chatBox.style.display = "flex";
  } else {
    chatBox.style.display = "none";
  }

  toggleBtn.onclick = () => {
    const isOpen = chatBox.style.display === "flex";
    chatBox.style.display = isOpen ? "none" : "flex";
    localStorage.setItem("chatOpen", !isOpen);
  };

  sendBtn.onclick = async () => {
    const message = input.value.trim();
    if (!message) return;

    msgBox.innerHTML += `<div><b>You:</b> ${message}</div>`;
    input.value = "";

    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    msgBox.innerHTML += `<div><b>AI:</b> ${data.reply}</div>`;
    msgBox.scrollTop = msgBox.scrollHeight;
  };
});
