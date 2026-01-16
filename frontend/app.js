const API_BASE = ""; // same origin

async function postJSON(url, payload) {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return { status: res.status, data: await res.json() };
}

async function runTest() {
  resetErrors();

  const input = document.getElementById("user-input").value.trim();
  if (!input) return;

  // --- Baseline ---
  try {
    const r = await postJSON("/baseline", { input });
    if (r.status === 200) {
      document.getElementById("baseline-response").innerText = r.data.response;
    } else {
      throw r.data;
    }
  } catch (e) {
    document.getElementById("baseline-error").innerText =
      "Error: " + (e.details || "Request failed");
  }

  // --- Guardrail ---
  try {
    const r = await postJSON("/generate", { input });

    if (r.status === 200) {
      document.getElementById("guardrail-response").innerText = r.data.response;

      const rp = document.getElementById("routing-path");
      const mi = document.getElementById("model-invoked");
      const note = document.getElementById("boundary-note");

      rp.innerText = r.data.routing_path;
      mi.innerText = r.data.model_invoked;

      if (r.data.routing_path === "dependency_boundary") {
        rp.className = "orange";
        mi.className = "red";
        note.innerText = "Boundary enforced before model invocation.";
      } else {
        rp.className = "green";
        mi.className = "green";
        note.innerText = "";
      }
    } else {
      throw r.data;
    }
  } catch (e) {
    document.getElementById("guardrail-error").innerText =
      "Error: " + (e.details || "Request failed");
  }
}

function resetState() {
  document.getElementById("baseline-response").innerHTML =
    '<span class="placeholder">response</span>';
  document.getElementById("guardrail-response").innerHTML =
    '<span class="placeholder">response</span>';

  document.getElementById("routing-path").innerText = "—";
  document.getElementById("model-invoked").innerText = "—";
  document.getElementById("boundary-note").innerText = "";

  resetErrors();
}

function resetErrors() {
  document.getElementById("baseline-error").innerText = "";
  document.getElementById("guardrail-error").innerText = "";
}
