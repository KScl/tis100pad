"use strict";

window.addEventListener("load", 
  function() { 
    var form = document.getElementById("nodes");
    var execbuttons = form.getElementsByClassName("exec");
    var stckbuttons = form.getElementsByClassName("stck");
    var errbuttons = form.getElementsByClassName("err");
    var textareas = form.getElementsByTagName("textarea");
    
    for (var i = 0; i < execbuttons.length; i++) {
      execbuttons[i].addEventListener("click", makeNodeExec, false);
    }
    
    for (var i = 0; i < stckbuttons.length; i++) {
      stckbuttons[i].addEventListener("click", makeNodeStck, false);
    }
    
    for (var i = 0; i < errbuttons.length; i++) {
      errbuttons[i].addEventListener("click", makeNodeErr, false);
    }
    
    for (var i = 0; i < textareas.length; i++) {
      textareas[i].value = "";
      textareas[i].addEventListener("keypress", limitText, false);
      textareas[i].addEventListener("paste", trimText, false);
    }
    
    var fileinput = document.getElementById("uploadbutton").getElementsByTagName("input")[0];
    fileinput.addEventListener("change", uploadFile, false);
    document.getElementById("savebutton").addEventListener("click", submitSolution, false);
    document.getElementById("uploadbutton").addEventListener("click", function() {
      fileinput.click();
    }, false);
    document.getElementById("newbutton").addEventListener("click", clearScreen, false);
    
    if (window.location.pathname !== "" && window.location.pathname !== "/") {
      loadSolution();
    }
  }, false);
  
function makeNodeExec() {
  var node = this.parentNode.parentNode;
  node.classList.remove("stcknode");
  node.classList.remove("errnode");
  node.classList.add("execnode");

  var textarea = node.getElementsByTagName("textarea")[0];
  if (textarea.savedValue) {
    textarea.value = textarea.savedValue;
  } else {
    textarea.value = "";
  }
  textarea.disabled = false;
  textarea.focus();
}
  
function makeNodeStck() {
  var node = this.parentNode.parentNode;
  var textarea = node.getElementsByTagName("textarea")[0];
  if (node.classList.contains("execnode")) {
    textarea.savedValue = textarea.value;
  }
  node.classList.add("stcknode");
  node.classList.remove("errnode");
  node.classList.remove("execnode");

  textarea.value = "\n\n\n\n\n█████████████████\n\nSTACK MEMORY NODE\n\n█████████████████";
  textarea.disabled = true;
}

function makeNodeErr() {
  var node = this.parentNode.parentNode;
  var textarea = node.getElementsByTagName("textarea")[0];
  if (node.classList.contains("execnode")) {
    textarea.savedValue = textarea.value;
  }
  node.classList.remove("stcknode");
  node.classList.add("errnode");
  node.classList.remove("execnode");

  textarea.value = "\n\n\n\n██████████████\n\nCOMMUNICATION\nFAILURE\n\n██████████████";
  textarea.disabled = true;
}

// Adapted from https://developer.mozilla.org/en-US/docs/Web/API/HTMLTextAreaElement#Maximum_length_and_number_of_lines_example
function limitText(e) {
  var	nKey = e.keyCode,
  nCols = this.cols,
  nRows = this.rows,
  nSelS = this.selectionStart, nSelE = this.selectionEnd,
  sVal = this.value, nLen = sVal.length,
  nBackward = nSelS >= nCols ? nSelS - nCols : 0,
  nDeltaForw = sVal.substring(nBackward, nSelS).search(new RegExp("\\n(?!.{0," + String(nCols - 2) + "}\\n)")) + 1,
  nRowStart = nBackward + nDeltaForw,
  aReturns = (sVal.substring(0, nSelS) + sVal.substring(nSelE, sVal.length)).match(/\n/g),
  nRowEnd = nSelE + nRowStart + nCols - nSelS,
  sRow = sVal.substring(nRowStart, nSelS) + sVal.substring(nSelE, nRowEnd > nLen ? nLen : nRowEnd),
  bKeepCols = nKey === 13 || nLen + 1 < nCols || /\n/.test(sRow) || ((nRowStart === 0 || nDeltaForw > 0 || nKey > 0) && (sRow.length < nCols || (nKey > 0 && (nLen === nRowEnd || sVal.charAt(nRowEnd) === "\n"))));
  if (!((nKey !== 13 || (aReturns ? aReturns.length + 1 : 1) < nRows) && ((nKey > 32 && nKey < 41) || bKeepCols))) {
    e.preventDefault();
  }
}

function trimText(e) {
  var rows = this.rows;
  var cols = this.cols;
  var text = this.value;
  var pastedText = e.clipboardData.getData('text/plain');
  var newText = getNewText(text, pastedText, this.selectionStart, this.selectionEnd);
  var lines = newText.split("\n");
  var lineTooLong = false;
  for (var i = 0; i < lines.length; i++) {
    if (lines[i].length > cols) {
      lineTooLong = true;
      break;
    }
  }
  if (lineTooLong || lines.length > rows) {
    e.preventDefault();
  } else {
    return;
  }
  if (lines.length > rows) {
    lines = lines.slice(0, rows);
  }
  if (lineTooLong) {
    for (var i = 0; i < lines.length; i++) {
      if (lines[i].length > cols) {
        lines[i] = lines[i].slice(0, cols);
      }
    }
  }
  newText = "";
  for (var i = 0; i < lines.length; i++) {
    newText = newText + lines[i];
    if (i !== lines.length - 1) {
      newText = newText + "\n";
    }
  }
  this.value = newText;
  
  function getNewText(oText, pText, selStart, selEnd) {
    var startClear = (selStart < selEnd) ? selStart : selEnd;
    var endClear = (selStart < selEnd) ? selEnd : selStart;
    var nText = oText.slice(0, startClear) + pText + oText.slice(endClear);
    return nText;
  }
}

function displayMessage(message) {
  var statusmessage = document.getElementById("statusmessage");
  statusmessage.innerHTML = message;
  setTimeout(function() {
    statusmessage.innerHTML = "";
  }, 5000);
}

function submitSolution() {
  var form = document.getElementById("nodes");
  var textareas = form.getElementsByTagName("textarea");
  var blank = true;
  for (var i = 0; i < textareas.length; i++) {
    if (textareas[i].value !== "" && textareas[i].parentNode.classList.contains("execnode")) {
      blank = false;
      break;
    }
  }
  if (blank) {
    window.displayMessage("NO CHANGES TO SAVE");
    return;
  }
  var XHR = new XMLHttpRequest();
  var disabledlist = [];
  for (var i = 0; i < textareas.length; i++) {
    if (textareas[i].disabled) {
      textareas[i].readonly = true;
      textareas[i].disabled = false;
      disabledlist.push(textareas[i])
    }
  }
  var FD = new FormData(form);
  for (var i = 0; i < disabledlist.length; i++) {
    disabledlist[i].disabled = true;
    disabledlist[i].readonly = false;
  }
  var path = window.location.pathname.split("/");
  var master = path[1] ? path[1] : "0";
  FD.append("master", master);
  XHR.addEventListener("load", confirmSubmit, false);
  XHR.addEventListener("error", submitError, false);
  XHR.open("POST", "/db/submit");
  XHR.send(FD);
  
  function confirmSubmit() {
    if (this.status === 200) {
      var response = this.responseText.split("/");
      var newUrl = "/" + response[0];
      if (parseInt(response[1])) {
        newUrl = newUrl + "/" + response[1];
      }
      window.history.replaceState("TIS-100 NOTEPAD", "", newUrl);
      window.displayMessage("SOLUTION SAVED");
    } else if (this.status === 202) {
      window.displayMessage("NO CHANGES TO SAVE");
    } else {
      submitError();
    }
  }
  
  function submitError() {
    window.displayMessage("SUBMISSION ERROR. PLEASE TRY AGAIN.");
  }
}

function loadSolution() {
  var path = window.location.pathname.split("/");
  var master = path[1];
  var forkno = path[2] ? path[2] : "0";
  var requestPath = path[2] ? "/db/" + path[1] + "/" + path[2] : "/db/" + path[1];
  var XHR = new XMLHttpRequest();
  var FD = new FormData(document.getElementById("nodes"));
  FD.append("master", master);
  FD.append("forkno", forkno);
  XHR.addEventListener("load", insertLoadedSolution, false);
  XHR.addEventListener("error", loadError, false);
  XHR.open("POST", requestPath);
  XHR.send(FD);
  
  function insertLoadedSolution() {
    if (this.status === 200) {
      var response = JSON.parse(this.responseText);
      fillSolution(response);
    } else if (this.status === 404) {
      window.displayMessage("SOLUTION NOT FOUND")
      window.history.replaceState("TIS-100 NOTEPAD", "", "/");
    } else {
      loadError();
    }
  }
  
  function loadError() {
    window.displayMessage("ERROR LOADING SOLUTION. PLEASE TRY AGAIN.");
    window.history.replaceState("TIS-100 NOTEPAD", "", "/");
  }
}

function uploadFile() {
  var file = this.files[0];
  var XHR = new XMLHttpRequest();
  var FD = new FormData();
  FD.append("file", file);
  XHR.addEventListener("load", loadFileData, false);
  XHR.addEventListener("error", uploadError, false);
  XHR.open("POST", "/db/upload");
  XHR.send(FD);
  
  function loadFileData() {
    if (this.status === 200) {
      var response = JSON.parse(this.responseText);
      fillSolution(response);
    } else if (this.status === 400) {
      window.displayMessage("INVALID SAVE FILE");
    } else {
      uploadError();
    }
  }
  
  function uploadError() {
    window.displayMessage("FILE UPLOAD ERROR. PLEASE TRY AGAIN.");
  }
}

function clearScreen() {
  var textareas = document.getElementById("nodes").getElementsByTagName("textarea");
  for (var i = 0; i < textareas.length; i++) {
    textareas[i].parentNode.getElementsByClassName("exec")[0].click();
    textareas[i].value = "";
  }
  if (window.location.pathname !== "" && window.location.pathname !== "/") {
    window.history.pushState("TIS-100 NOTEPAD", "", "/");
  }
}

function fillSolution(solution) {
  var textareas = document.getElementById("nodes").getElementsByTagName("textarea");
  for (var i = 0; i < textareas.length; i++) {
    textareas[i].parentNode.getElementsByClassName("exec")[0].click();
    var thisnode = solution[textareas[i].name];
    if (thisnode === undefined) {
      textareas[i].value = "";
    } else {
      textareas[i].value = solution[textareas[i].name].trim();
    }
    if (textareas[i].value === "█████████████████\n\nSTACK MEMORY NODE\n\n█████████████████") {
      textareas[i].value = "";
      textareas[i].parentNode.getElementsByClassName("stck")[0].click();
    }
    if (textareas[i].value === "██████████████\n\nCOMMUNICATION\nFAILURE\n\n██████████████") {
      textareas[i].value = "";
      textareas[i].parentNode.getElementsByClassName("err")[0].click();
    }
  }
}