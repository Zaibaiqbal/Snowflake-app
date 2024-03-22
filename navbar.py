

def render_navbar():
# Navbar
    nav_items = {
        "Partners": "/Partners",
        "shared": "/shared",
        "operations": "/operations",
        "Account": "/Account",
        "Message": "/Message",
        "profile": "/profile",
    }

# Generate HTML links for navbar items
    nav_links = ''.join(f'<a href="{url}">{label}</a>' for label, url in nav_items.items())

    navbar_template = f"""
        <style>
            .navbar {{
                background-color:#74A7C3;
                display: flex;
                align-items: center;
                width: 60%; 
                height:10%;
                margin: 0;
                position: fixed; 
                top: 39px; 
            
            }}

            .navbar a {{
                color: #fffff;
                text-align: center;
                text-decoration: none;
                font-size: 17px;
                padding: 14px 20px;
            
            }}

            .navbar a:hover {{
                background-color: #ddd;
                color: black;
            }}
        </style>
        <div class="navbar">
            {nav_links}
        </div>
    """

    return navbar_template

