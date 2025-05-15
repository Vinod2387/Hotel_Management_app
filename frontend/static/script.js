document.getElementById("guestForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const form = e.target;
    const data = new URLSearchParams(new FormData(form));
    const res = await fetch("/guest", {
        method: "POST",
        body: data,
    });
    if (res.ok) {
        location.reload();
    } else {
        alert("Failed to add guest.");
    }
});