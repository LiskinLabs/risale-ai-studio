import re
import html as html_mod

# Read the extracted text
with open(r'C:\Users\silvestr.liskin\Desktop\risale-ai-studio\altinci_from_html.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Clean up the text
# 1. Remove HTML tags and attributes
text = re.sub(r'<[^>]+>', ' ', text)
# 2. Unescape HTML entities
text = html_mod.unescape(text)
# 3. Remove remaining data-* attributes
text = re.sub(r'data-[a-z]+="[^"]*"', '', text)
text = re.sub(r'data-[a-z]+=\'[^\']*\'', '', text)
# 4. Fix spacing around punctuation
text = re.sub(r' ([.,!?;:)\]])', r'\1', text)
text = re.sub(r'([\[(]) ', r'\1', text)
# 5. Fix Turkish quote spacing
text = text.replace(' “ ', '“')
text = text.replace(' ” ', '” ')
text = text.replace(' ‘ ', '‘')
text = text.replace(' ’ ', '’ ')
# 6. Replace multiple spaces with single space
text = re.sub(r' {2,}', ' ', text)
# 7. Fix ellipsis style
text = re.sub(r'\.\s*\.\s*\.', '...', text)
# 8. Remove leading/trailing whitespace per line
lines = text.split('\n')
lines = [l.strip() for l in lines]
text = '\n'.join(lines)
# Replace multiple newlines with double
text = re.sub(r'\n{3,}', '\n\n', text)

# Final cleanup of remaining artifacts
# Remove ALL remaining HTML fragments and data attributes
text = re.sub(r'<[^>]+>', '', text)
text = re.sub(r'\s*data-[a-z]+="[^"]*"\s*', ' ', text)
text = re.sub(r'\s*data-[a-z]+=\'[^\']*\'\s*', ' ', text)
# Remove leading junk characters (Nefis" data-... artifacts)
text = re.sub(r'^.*?"\s*>?\s*', '', text)  # Remove everything up to and including the first > after Nefis
# Fix quote spacing throughout
text = text.replace(':"', ': "')
text = re.sub(r' ([:;,.!?])', r'\1', text)
# Add space after closing quotes where needed
text = re.sub(r'”([A-Za-z])', r'” \1', text)
text = re.sub(r'”([ÇçĞğİıÖöŞşÜü])', r'” \1', text)
# Remove leading/trailing whitespace
text = text.strip()

# Write cleaned version
with open(r'C:\Users\silvestr.liskin\Desktop\risale-ai-studio\altinci_soz_clean.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print('Wrote', len(text), 'chars')
