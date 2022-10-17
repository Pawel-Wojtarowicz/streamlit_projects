import streamlit as st
import os
import rebrick
import json

rebrick.init("8e81bf52ab2d71baadb63847e48d5035")

if "response" not in st.session_state:
    st.session_state.response = rebrick.lego.get_set_alternates(42110)

def main():
    st.sidebar.success("Select project above.")
    css_path = "styles/main.css"
    abs_path = os.path.abspath(css_path)
    # rebrick.init("8e81bf52ab2d71baadb63847e48d5035")

    with open(abs_path) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)
    
 
    title = '<p style="color:White; font-size: 30px;">With this app you can find alternative LEGO sets with <a href="https://rebrickable.com/">"REBRICKABLE API"</a></p>'
    st.markdown(title, unsafe_allow_html=True)
    
    provided_lego_set = 42100
    with st.form(key="myform"):
        provided_lego_set = st.number_input(label="Enter LEGO set", value=42100, step=1)
        st.form_submit_button("Find a MOC")


    try:
        st.session_state.response = rebrick.lego.get_set_alternates(provided_lego_set)
        results = json.loads(st.session_state.response.read())
        if results['count'] == 0:
            st.error("No MOC for provided LEGO set")
        else:
            mocs = results["results"]
            names = ([d["name"] for d in mocs])
            img_url = ([d["moc_img_url"] for d in mocs])
            moc_url = ([d["moc_url"] for d in mocs])
            mocs_dict = {key: value for key, *
                            value in zip(names, img_url, moc_url)}

            for key, value in mocs_dict.items():
                st.write(key)
                st.write(f"[![zdj]({value[0]})]({value[1]})")

    except:
        pass


if __name__ == "__main__":
    main()
