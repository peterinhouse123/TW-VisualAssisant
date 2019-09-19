const { app, BrowserWindow } = require('electron')

function createWindow () {
  // Create the browser window.
//   let win = new BrowserWindow({
//     width: 350,
//     height: 600,
//     titleBarStyle: 'hiddenInset' ,
//     webPreferences: {
//       nodeIntegration: true
//     }
//   })
    let win = new BrowserWindow({ transparent: true, frame: false })
  // and load the index.html of the app.
  // win.webContents.openDevTools()
  win.setMenu(null);
  win.loadFile('index.html')
}

app.on('ready', createWindow)