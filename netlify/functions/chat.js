const https = require("https");

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method Not Allowed" };
  }

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return { statusCode: 500, body: JSON.stringify({ error: "API key not configured" }) };
  }

  let body;
  try {
    body = JSON.parse(event.body);
  } catch {
    return { statusCode: 400, body: JSON.stringify({ error: "Invalid JSON" }) };
  }

  const payload = JSON.stringify({
    model: "claude-haiku-4-5-20251001",
    max_tokens: 1024,
    system: body.system || "You are Carrie, a warm and efficient AI executive assistant.",
    messages: body.messages || [],
  });

  return new Promise((resolve) => {
    const req = https.request(
      {
        hostname: "api.anthropic.com",
        path: "/v1/messages",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": apiKey,
          "anthropic-version": "2023-06-01",
          "Content-Length": Buffer.byteLength(payload),
        },
      },
      (res) => {
        let data = "";
        res.on("data", (chunk) => (data += chunk));
        res.on("end", () => {
          try {
            const parsed = JSON.parse(data);
            if (parsed.content && parsed.content[0]) {
              resolve({
                statusCode: 200,
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ content: parsed.content[0].text }),
              });
            } else {
              resolve({ statusCode: 502, body: JSON.stringify({ error: "Unexpected API response", raw: data }) });
            }
          } catch {
            resolve({ statusCode: 502, body: JSON.stringify({ error: "Failed to parse API response" }) });
          }
        });
      }
    );

    req.on("error", (err) => {
      resolve({ statusCode: 502, body: JSON.stringify({ error: err.message }) });
    });

    req.write(payload);
    req.end();
  });
};
