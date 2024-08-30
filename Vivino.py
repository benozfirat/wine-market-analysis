import streamlit as st


# Set the page title and icon
st.set_page_config(page_title="Vivino Homepage", page_icon="🍷")

# Add the logo image
st.image("utils/images/Vivino.png", width=200)


st.markdown("""
<h1 align="center">🍷 Vivino Project🍷</h1>
""", unsafe_allow_html=True)




# Display a quick intro
# Display title of the page
st.markdown("## Welcome to our homepage! 🏠")

st.markdown("""
We are a distinguished wine-selling company with deep roots in the historic city of Liège, where we have been proudly established since 2036. Over the years, we have grown from a small, passionate team into a globally recognized brand, known for our commitment to quality and innovation in the wine industry.

Our unique office is located at the Pôle Image, a creative hub that embodies our innovative spirit. Hidden beneath the trapdoor in Ben's office, our workspace is a blend of tradition and modernity, reflecting our dedication to preserving the rich heritage of winemaking while embracing the future.

At Vivino, we are honored to partner with over 10,000 esteemed wine producers from across the world. This extensive network allows us to offer a diverse selection of exceptional wines, catering to connoisseurs and casual enthusiasts alike. Our commitment to excellence ensures that every bottle we sell is a testament to the artistry and passion of the winemakers we represent.

From the rolling vineyards of Europe to the emerging wine regions of the New World, our products reach wine lovers in every corner of the globe, bringing the finest selections to your table.
""")

# Display first image
st.image("utils/images/Mr.Geppetto.jpeg", caption="Mr.Geppetto, our founder", use_column_width=True, width=100)


st.markdown("---")

# Display a new paragraph title
st.markdown("## Our Story 📖")

# Display the story
st.markdown("""
Vivino's origins trace back to Mr. Geppetto, an old Italian man with a remarkable talent for wine tasting and business acumen.
Originally from Italy, Mr. Geppetto's family owned a vineyard for centuries. In 2035, he moved to Belgium, where he decided to harness his expertise in wine to establish a company. 
His vision and passion for wine led to the creation of Vivino, a company that blends innovation with tradition to offer exceptional wine experiences.
""")

# Display second image
st.image("utils/images/Geppetto_Pinocchio.jpeg", caption="Geppetto and his son in the family vineyard", use_column_width=True, width=100)


st.markdown("---")

# Display new paragraph title
st.markdown("## Our Team 👨‍👨‍👦‍👦")

# Display the team paragraph
st.markdown("""Vivino is now under the control of four individuals who fervently profess their commitment to revitalizing the wine market, promising a fusion of innovation and tradition that will redefine the industry. They declare their mission to restore the wine market to its former glory, but beneath the veneer of their noble rhetoric lies a stark truth. Their grand promises of unparalleled experiences are overshadowed by a more insidious reality: a relentless pursuit of money and fame. While they project an image of passion and dedication, their true drive is a quest for personal gain and public acclaim. The facade of their purported vision masks the cold reality of their ambitions.""")

# Display third image
st.image("utils/images/Dalton.jpg", caption="Actual Team", use_column_width=True)


# Display a footer with links to our GitHub profiles

st.write("### Meet the Team")
st.write("""

- [Geoffroy Panis](https://github.com/Jojopanis) - Data Engineer
- [Ben Ozfirat](https://github.com/benozfirat) - Data Analyst
- [Hui Shang](https://github.com/EmmaSHANG0625) - Data Analyst
- [Colin Grégoire](https://github.com/Atome1212) - Data Engineer
""")

st.markdown("---") 

st.write("""          
&copy; 2056 ThisIsNotReallyVivino. All rights reserved.
""")
