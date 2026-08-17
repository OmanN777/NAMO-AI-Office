const fs = require('fs');
const path = require('path');

const replacements = {
    'เทสต์': 'test',
    'เทส': 'test',
    'โปรเจกต์': 'project',
    'โปรเจ็ค': 'project',
    'โปรเจค': 'project',
    'สคริปต์': 'script',
    'คอมเมนต์': 'comment',
    'คอนเซปต์': 'concept',
    'เซิร์ฟเวอร์': 'server',
    'อัลกอริทึม': 'algorithm',
    'แพลตฟอร์ม': 'platform',
    'เบราว์เซอร์': 'browser',
    'อัปเดต': 'update',
    'อัพเดท': 'update',
    'เวอร์ชัน': 'version',
    'เวอร์ชั่น': 'version',
    'ฟีเจอร์': 'feature',
    'โค้ด': 'code',
    'รีเควสต์': 'request',
    'บั๊ก': 'bug',
    'แอปพลิเคชัน': 'application'
};

function walkSync(currentDirPath, callback) {
    fs.readdirSync(currentDirPath).forEach(function (name) {
        const filePath = path.join(currentDirPath, name);
        const stat = fs.statSync(filePath);
        if (stat.isFile()) {
            callback(filePath, stat);
        } else if (stat.isDirectory() && name !== 'node_modules' && name !== '.git') {
            walkSync(filePath, callback);
        }
    });
}

walkSync('.', function(filePath, stat) {
    if (filePath.endsWith('.md') || filePath.endsWith('.ts') || filePath.endsWith('.txt')) {
        let content = fs.readFileSync(filePath, 'utf8');
        let modified = false;
        
        for (const [key, value] of Object.entries(replacements)) {
            // Use positive lookbehind and lookahead for non-Thai characters if possible, 
            // but since Thai doesn't use spaces, it's hard. 
            // The terms chosen are fairly unique.
            // Exclude 'เทส' if it's followed by 'ติ้ง' or something, but 'testติ้ง' is fine.
            // 'ประเทศ' ends in 'เทศ' so 'เทส' won't match 'เทศ'.
            const regex = new RegExp(key, 'g');
            if (regex.test(content)) {
                content = content.replace(regex, value);
                modified = true;
            }
        }
        
        if (modified) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log('Updated: ' + filePath);
        }
    }
});
