// Simple test to verify navigation routes exist
const fs = require('fs');
const path = require('path');

const tabsDir = path.join(__dirname, 'app', '(tabs)');
const requiredFiles = ['index.tsx', 'livetracker.tsx', 'outbreakdetails.tsx', 'safetytips.tsx', '_layout.tsx'];

console.log('Checking navigation files...');
requiredFiles.forEach(file => {
  const filePath = path.join(tabsDir, file);
  if (fs.existsSync(filePath)) {
    console.log(`✓ ${file} exists`);
  } else {
    console.log(`✗ ${file} missing`);
  }
});

console.log('\nChecking app structure...');
const appLayoutPath = path.join(__dirname, 'app', '_layout.tsx');
if (fs.existsSync(appLayoutPath)) {
  console.log('✓ Root layout exists');
} else {
  console.log('✗ Root layout missing');
}
