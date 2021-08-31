mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"paredeslm.ca@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]
primaryColor = '#575fe8'/n
backgroundColor = '#f5f7f3'\n
secondaryBackgroundColor = '#c9eab8'\n
textColor = '#262730'\n
font = 'sans serif'\n
" > ~/.streamlit/config.toml
