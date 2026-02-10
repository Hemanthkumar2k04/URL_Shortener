async function generateShortUrl() {
  const longUrl = document.getElementById("longUrl").value;
  const resultBox = document.getElementById("resultBox");
  const shortenBtn = document.getElementById("shortenBtn");
  
  // Reset result box
  resultBox.className = "result";
  resultBox.innerHTML = "";
  resultBox.classList.remove("show", "error", "success");
  
  if (!longUrl) {
    resultBox.innerHTML = "❌ Please enter a URL!";
    resultBox.classList.add("show", "error");
    return;
  }
  
  // Basic URL validation
  try {
    new URL(longUrl);
  } catch (_) {
    resultBox.innerHTML = "❌ Please enter a valid URL (include http:// or https://)";
    resultBox.classList.add("show", "error");
    return;
  }
  
  // Show loading state
  const originalBtnText = shortenBtn.innerHTML;
  shortenBtn.innerHTML = '<span class="loading"></span> Shortening...';
  shortenBtn.disabled = true;
  
  try {
    const res = await fetch("http://127.0.0.1:8000/shorten", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ original_url: longUrl })
    });

    const data = await res.json();

    if (!res.ok) {
      resultBox.innerHTML = `❌ Error: ${data.detail || "Unknown error"}`;
      resultBox.classList.add("show", "error");
      return;
    }

    const shortUrl = `http://127.0.0.1:8000/${data.short_code}`;
    resultBox.innerHTML = `
      ✅ Short URL created!<br><br>
      <strong>Original:</strong><br>
      <span style="color: #666; font-size: 13px;">${longUrl}</span><br><br>
      <strong>Shortened:</strong><br>
      <a href="${shortUrl}" target="_blank">${shortUrl}</a>
      <br><br>
      <button class="copy-btn" onclick="copyToClipboard('${shortUrl}')">📋 Copy Short URL</button>
    `;
    resultBox.classList.add("show", "success");
    
  } catch (err) {
    resultBox.innerHTML = "⚠️ Server not running or network error!";
    resultBox.classList.add("show", "error");
  } finally {
    // Reset button
    shortenBtn.innerHTML = originalBtnText;
    shortenBtn.disabled = false;
  }
}

// Helper function to copy to clipboard
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert("✅ Copied to clipboard!");
  });
}

// Handle Enter key press
function handleEnter(event) {
  if (event.key === "Enter") {
    generateShortUrl();
  }
}