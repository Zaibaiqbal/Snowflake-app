def generate_header_html():
    nav_items = {
        "Partners": "/Partners",
        "Shared": "/shared",
        "Operations": "/operations",
        "Account": "/Account",
        "Message": "/Message",
        "Profile": "/profile",
    }

    # Generate HTML links for navbar items
    nav_links = ''.join(f'<a href="{url}" style="color: purple; margin: 0 10px;">{label}</a>' for label, url in nav_items.items())

    navbar_template = f"""
        <style>
            .navbar {{
                display: flex;
                justify-content: center;
                align-items: right;
                width: 100%;
                padding: 10px 0;
                margin: 0;
                position: fixed;
                top: 25;
                left: 110px;
                right: 0;
                z-index: 999;
                background-color: none; 
            }}

            .navbar a {{
                color: purple; 
                text-decoration: none;
                font-size: 17px;
                padding: 10px 30px; 
            }}
        </style>
        <div class="navbar">
            {nav_links}
        </div>
    """
    return navbar_template
