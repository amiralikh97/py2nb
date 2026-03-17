const vscode = require('vscode');
const { exec } = require('child_process');
const path = require('path');

function activate(context) {
    const disposable = vscode.commands.registerCommand('py2nb.convert', () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('py2nb: no active editor');
            return;
        }

        const inputPath = editor.document.uri.fsPath;
        if (!inputPath.endsWith('.py')) {
            vscode.window.showErrorMessage('py2nb: active file is not a .py file');
            return;
        }

        editor.document.save().then(() => {
            const dir = path.dirname(inputPath);
            const stem = path.basename(inputPath, '.py');
            const outputPath = path.join(dir, stem + '_py2nb.ipynb');

            // Use bundled Python source — no pip install required
            const scriptPath = path.join(context.extensionPath, 'py2nb', 'cli.py');

            const config = vscode.workspace.getConfiguration('py2nb');
            const python = config.get('pythonPath') || 'python';

            const cmd = `"${python}" "${scriptPath}" "${inputPath}" -o "${outputPath}"`;

            exec(cmd, { cwd: dir }, (error, stdout, stderr) => {
                if (error) {
                    vscode.window.showErrorMessage(
                        `py2nb failed: ${(stderr || error.message).trim()}`
                    );
                    return;
                }

                vscode.window.showInformationMessage(
                    `py2nb: written ${path.basename(outputPath)}`,
                    'Open'
                ).then(choice => {
                    if (choice === 'Open') {
                        vscode.commands.executeCommand(
                            'vscode.open',
                            vscode.Uri.file(outputPath)
                        );
                    }
                });
            });
        });
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = { activate, deactivate };
