import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
export { loadMermaid, onRevealReady };

/**
 * Alter all ids in the svg adding the index of the graph.
 * Make sure that the style is updated to use the new ids.
 * @param {string} svgString string of the mermaid svg
 * @param {number} idx index of the graph. Used to make the ids unique
 * @returns {string} string of the mermaid svg with updated ids
 */
function uniqueIds(svgString, idx) {
  /** @type {Set<string>} */
  const set = new Set();
  // Find al the marker ids in the svg and replace them with `id-${idx}`
  svgString = svgString.replace(
    /<marker.*?id=['"]([^"']+)["'].*?<\/marker>/g,
    (match, id) => {
      set.add(id);
      return match.replace(id, `${id}-${idx}`);
    }
  );
  if (set.size === 0) return svgString;
  // If some ids were found, replace them in the rest of the svg
  const re = new RegExp(`#(${Array.from(set.values()).join("|")})`, "g");
  return svgString.replace(re, `#$1-${idx}`);
}

/**
 * Find all elements with the class mermaid and ensure that they are rendered
 * correctly by manually ensuring that the internal ids of the rendered svg
 * are unique.
 * If an error occurs during rendering, the error is logged to the console and
 * the graph is not rendered.
 */
function mermaidParser() {
  const graphs = document.getElementsByClassName("mermaid");
  graphs.forEach(async (item, index) => {
    const graphCode = item.textContent.trim();
    const mermaidDiv = document.createElement("div");
    mermaidDiv.classList.add("mermaid");
    mermaidDiv.setAttribute("data-processed", "true");

    try {
      const { svg } = await mermaid.render(`graph-${index}`, graphCode);
      mermaidDiv.innerHTML = uniqueIds(svg, index);
      item.parentNode.parentNode.insertBefore(mermaidDiv, item.parentNode);
      // If the graph was a fragment, carry it to the rendered svg
      if (item.parentNode.classList.contains("fragment")) {
        mermaidDiv.classList.add("fragment");
      }
      item.parentNode.remove();
    } catch (err) {
      console.error(`Cannot render diagram ${index}\n${graphCode}`);
      console.error(err.message);
    }
  });
}
/**
 * Add support for math block environments in markdown.
 * The environment is indicated by ```math ... ``` blocks.
 */
function mathBlockParser() {
  const maths = document.getElementsByClassName("math");
  maths.forEach(async (item) => {
    const mathDiv = document.createElement("p");
    const mathCode = item.textContent.trim();
    mathDiv.classList.add("math");
    mathDiv.innerText = `$$\n${mathCode}\n$$`;

    item.parentNode.parentNode.insertBefore(mathDiv, item.parentNode);
    item.parentNode.remove();
  });
}

/**
 * Add support for math dollar environment in markdown.
 * The environment is indicated by $$ ... $$.
 */
function mathDollarParser() {
  const maths = document.evaluate(
    '//p[starts-with(., "$$")]',
    document,
    null,
    XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE,
    null
  );
  for (let i = 0; i < maths.snapshotLength; i++) {
    // Substitute any <em> tags with _ to avoid conflicts with markdown
    maths.snapshotItem(i).innerHTML = maths
      .snapshotItem(i)
      .innerHTML.replace(/<em>/g, "_")
      .replace(/<\/em>/g, "_");

    const codeEl = document.createElement("code");
    codeEl.innerHTML = maths.snapshotItem(i).textContent;
    maths.snapshotItem(i).innerHTML = "";
    maths.snapshotItem(i).appendChild(codeEl);
  }
}

/** Initialize mermaid with custom settings. */
function loadMermaid() {
  mermaid.initialize({
    startOnLoad: false,
    theme: "dark",
    flowchart: { htmlLabels: false },
  });
}

/** Render all qrcode tags by creating the corresponding qr code. */
function renderUrlToQr() {
  const qrCodes = document.getElementsByTagName("qrcode");
  qrCodes.forEach((e) => {
    const url = e.getAttribute("url") ?? location.href;
    const size = e.getAttribute("size") ?? 128;
    const dark = e.getAttribute("dark") ?? "#000";
    const light = e.getAttribute("light") ?? "#fff";

    // Render the qr code on top the urltoqr element
    new QRCode(e, {
      text: url,
      width: parseInt(size),
      height: parseInt(size),
      colorDark: dark,
      colorLight: light,
      correctLevel: QRCode.CorrectLevel.H,
    });
    const qr = e.getElementsByTagName("img")[0];

    // Open the url in a new tab when the qr code is clicked
    qr.addEventListener("click", (e) => window.open(url, "_blank"));
    qr.style.cursor = "pointer";

    // Choose the alignment of the qr code
    const align = e.getAttribute("align") ?? "center";
    switch (align) {
      case "right":
        qr.style.marginLeft = "auto";
        break;
      case "center":
        qr.style.margin = "auto";
        break;
    }
  });
}

/** Initialize Reveal with support for personalized extensions. */
function onRevealReady(event) {
  mathBlockParser();
  mermaidParser();
  mathDollarParser();
  renderUrlToQr();
}

window.loadMermaid = loadMermaid;
Reveal.addEventListener("ready", onRevealReady);
