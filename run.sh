# need npm install reveal-md
if [ "$1" = "" ]; then
    echo "Usage: $0" file.md
    echo ""
    echo "With file one of" *.md
else
    npm i reveal-md
    ./node_modules/.bin/reveal-md $1 -w --theme simple --css static/fifix.css --highlight-theme github
fi
