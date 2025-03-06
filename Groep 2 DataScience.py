import streamlit as st
import pandas as pd
import plotly.express as px

# Lees de CSV in
def load_video_data():
    df = pd.read_csv('youtube.csv')  # Zorg ervoor dat het bestand op de juiste locatie staat
    df["country"] = df["region_code"].map(country_dict)
    return df

country_dict = {
    'AF': 'Afghanistan',
    'AL': 'Albanië',
    'DZ': 'Algerije',
    'AS': 'Amerikaans-Samoa',
    'AD': 'Andorra',
    'AO': 'Angola',
    'AI': 'Anguilla',
    'AQ': 'Antarctica',
    'AG': 'Antigua en Barbuda',
    'AR': 'Argentinië',
    'AM': 'Armenië',
    'AW': 'Aruba',
    'AU': 'Australië',
    'AT': 'Oostenrijk',
    'AZ': 'Azerbeidzjan',
    'BS': 'Bahama’s',
    'BH': 'Bahrain',
    'BD': 'Bangladesh',
    'BB': 'Barbados',
    'BY': 'Belarus',
    'BE': 'België',
    'BZ': 'Belize',
    'BJ': 'Benin',
    'BM': 'Bermuda',
    'BT': 'Bhutan',
    'BO': 'Bolivia',
    'BA': 'Bosnië en Herzegovina',
    'BW': 'Botswana',
    'BR': 'Brazilië',
    'IO': 'Britse Indische Oceaanterritorium',
    'BN': 'Brunei',
    'BG': 'Bulgarije',
    'BF': 'Burkina Faso',
    'BI': 'Burundi',
    'KH': 'Cambodja',
    'CM': 'Kameroen',
    'CA': 'Canada',
    'CV': 'Kaapverdië',
    'KY': 'Kaaimaneilanden',
    'CF': 'Centraal-Afrikaanse Republiek',
    'TD': 'Tsjaad',
    'CL': 'Chili',
    'CN': 'China',
    'CX': 'Christmaseiland',
    'CC': 'Cocoseilanden',
    'CO': 'Colombia',
    'KM': 'Comoren',
    'CG': 'Congo',
    'CD': 'Democratische Republiek Congo',
    'CK': 'Cookeilanden',
    'CR': 'Costa Rica',
    'CI': 'Ivoorkust',
    'HR': 'Kroatië',
    'CU': 'Cuba',
    'CW': 'Curaçao',
    'CY': 'Cyprus',
    'CZ': 'Tsjechië',
    'DK': 'Denemarken',
    'DJ': 'Djibouti',
    'DM': 'Dominica',
    'DO': 'Dominicaanse Republiek',
    'EC': 'Ecuador',
    'EG': 'Egypte',
    'SV': 'El Salvador',
    'GQ': 'Equatoriaal-Guinea',
    'ER': 'Eritrea',
    'EE': 'Estland',
    'SZ': 'Eswatini',
    'ET': 'Ethiopië',
    'FK': 'Falklandeilanden',
    'FO': 'Faeröer',
    'FJ': 'Fiji',
    'FI': 'Finland',
    'FR': 'Frankrijk',
    'GF': 'Frans-Guyana',
    'PF': 'Frans-Polynesië',
    'TF': 'Franse Zuidelijke en Antarctische Gebieden',
    'GA': 'Gabon',
    'GM': 'Gambia',
    'GE': 'Georgië',
    'DE': 'Duitsland',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GR': 'Griekenland',
    'GL': 'Groenland',
    'GD': 'Grenada',
    'GP': 'Guadeloupe',
    'GU': 'Guam',
    'GT': 'Guatemala',
    'GG': 'Guernsey',
    'GN': 'Guinee',
    'GW': 'Guinee-Bissau',
    'GY': 'Guyana',
    'HT': 'Haïti',
    'HM': 'Heard- en McDonaldeilanden',
    'HN': 'Honduras',
    'HK': 'Hongkong',
    'HU': 'Hongarije',
    'IS': 'IJsland',
    'IN': 'India',
    'ID': 'Indonesië',
    'IR': 'Iran',
    'IQ': 'Irak',
    'IE': 'Ierland',
    'IL': 'Israël',
    'IT': 'Italië',
    'JM': 'Jamaica',
    'JP': 'Japan',
    'JE': 'Jersey',
    'JO': 'Jordanië',
    'KZ': 'Kazachstan',
    'KE': 'Kenia',
    'KI': 'Kiribati',
    'KP': 'Noord-Korea',
    'KR': 'Zuid-Korea',
    'KW': 'Koeweit',
    'KG': 'Kirgizië',
    'LA': 'Laos',
    'LV': 'Letland',
    'LB': 'Libanon',
    'LS': 'Lesotho',
    'LR': 'Liberia',
    'LY': 'Libië',
    'LI': 'Liechtenstein',
    'LT': 'Litouwen',
    'LU': 'Luxemburg',
    'MO': 'Macau',
    'MG': 'Madagaskar',
    'MW': 'Malawi',
    'MY': 'Maleisië',
    'MV': 'Maldiven',
    'ML': 'Mali',
    'MT': 'Malta',
    'MH': 'Marshalleilanden',
    'MQ': 'Martinique',
    'MR': 'Mauritanië',
    'MU': 'Mauritius',
    'YT': 'Mayotte',
    'MX': 'Mexico',
    'FM': 'Micronesië',
    'MD': 'Moldavië',
    'MC': 'Monaco',
    'MN': 'Mongolië',
    'ME': 'Montenegro',
    'MS': 'Montserrat',
    'MA': 'Marokko',
    'MZ': 'Mozambique',
    'MM': 'Myanmar',
    'NA': 'Namibië',
    'NR': 'Nauru',
    'NP': 'Nepal',
    'NL': 'Nederland',
    'NC': 'Nieuw-Caledonië',
    'NZ': 'Nieuw-Zeeland',
    'NI': 'Nicaragua',
    'NE': 'Niger',
    'NG': 'Nigeria',
    'NU': 'Niue',
    'NF': 'Norfolkeiland',
    'MP': 'Noordelijke Marianen',
    'NO': 'Noorwegen',
    'OM': 'Oman',
    'PK': 'Pakistan',
    'PW': 'Palau',
    'PS': 'Palestina',
    'PA': 'Panama',
    'PG': 'Papoea-Nieuw-Guinea',
    'PY': 'Paraguay',
    'PE': 'Peru',
    'PH': 'Filipijnen',
    'PN': 'Pitcairn-eilanden',
    'PL': 'Polen',
    'PT': 'Portugal',
    'PR': 'Puerto Rico',
    'QA': 'Qatar',
    'RE': 'Réunion',
    'RO': 'Roemenië',
    'RU': 'Rusland',
    'RW': 'Rwanda',
    'BL': 'Saint-Barthélemy',
    'SH': 'Saint Helena',
    'KN': 'Saint Kitts en Nevis',
    'LC': 'Saint Lucia',
    'MF': 'Saint Martin',
    'SX': 'Sint Maarten',
    'SM': 'San Marino',
    'ST': 'Sao Tomé en Principe',
    'SA': 'Saoedi-Arabië',
    'SN': 'Senegal',
    'RS': 'Servië',
    'SC': 'Seychellen',
    'SL': 'Sierra Leone',
    'SG': 'Singapore',
    'SK': 'Slowakije',
    'SI': 'Slovenië',
    'SB': 'Salomonseilanden',
    'SO': 'Somalië',
    'ZA': 'Zuid-Afrika',
    'SS': 'Zuid-Soedan',
    'ES': 'Spanje',
    'LK': 'Sri Lanka',
    'SD': 'Soedan',
    'SR': 'Suriname',
    'SJ': 'Svalbard en Jan Mayen',
    'SE': 'Zweden',
    'CH': 'Zwitserland',
    'SY': 'Syrië',
    'TW': 'Taiwan',
    'TJ': 'Tadzjikistan',
    'TZ': 'Tanzania',
    'TH': 'Thailand',
    'TL': 'Timor-Leste',
    'TG': 'Togo',
    'TK': 'Tokelau',
    'TO': 'Tonga',
    'TT': 'Trinidad en Tobago',
    'TN': 'Tunesië',
    'TR': 'Turkije',
    'TM': 'Turkmenistan',
    'TC': 'Turkse eilanden',
    'TV': 'Tuvalu',
    'UG': 'Oeganda',
    'UA': 'Oekraïne',
    'AE': 'Verenigde Arabische Emiraten',
    'GB': 'Verenigd Koninkrijk',
    'US': 'Verenigde Staten',
    'UY': 'Uruguay',
    'UZ': 'Oezbekistan',
    'VU': 'Vanuatu',
    'VE': 'Venezuela',
    'VN': 'Vietnam',
    'WF': 'Wallis en Futuna',
    'EH': 'Westelijke Sahara',
    'YE': 'Jemen',
    'ZM': 'Zambia',
    'ZW': 'Zimbabwe'
}


# Functie voor de "Overview" pagina
def overview():
    st.title("Overview - Top 10 Video's")
    st.write("Dit is een overzichtspagina met de top 10 video's op basis van hun frequentie.")
    
    df = load_video_data()

    video_counts = df['video_id'].value_counts().reset_index()
    video_counts.columns = ['video_id', 'count']

    top_10_video_ids = video_counts.head(10)['video_id']
    top_10_videos = df[df['video_id'].isin(top_10_video_ids)]
    top_10_videos_info = top_10_videos[['title', 'channel_title', 'video_id']].drop_duplicates()
    top_10_videos_info = top_10_videos_info.merge(video_counts, on='video_id', how='left')
    top_10_videos_info_sorted = top_10_videos_info.sort_values(by='count', ascending=False)
    top_10_videos_info_sorted = top_10_videos_info_sorted.reset_index(drop=True)
    top_10_videos_info_sorted.index += 1

    st.write("Top 10 video's:")
    st.write(top_10_videos_info_sorted[['title', 'channel_title', 'count']])

    st.subheader("📊 Interactieve scatterplot")

    y_axis_option = st.radio(
        "📈 Selecteer de Y-as:",
        options=["likes", "comment_count", "subscribers"],
        format_func=lambda x: {"likes": "Likes", "comment_count": "Comments", "subscribers": "Abonnees"}[x],
        index=0
    )

    youtube = df.copy()

    continents = youtube["continent"].unique()
    continent_colors = {continent: i for i, continent in enumerate(continents)}
    youtube["continent_color"] = youtube["continent"].map(continent_colors)

    if youtube["views"].isna().sum() > 0 or youtube[y_axis_option].isna().sum() > 0:
        st.error("⚠ Er zitten ontbrekende waarden in de dataset, filter de data beter.")
    else:
        scatter_fig = px.scatter(
            youtube,
            x="views",
            y=y_axis_option,
            color="continent",
            color_discrete_sequence=px.colors.qualitative.Plotly,
            title=f"Views vs {y_axis_option.capitalize()} per Continent",
            log_x=True,
            log_y=True,
            #trendline="ols",
            trendline_color_override="black",
            hover_data={"title":True, "category_name":True,"country":True,"rank_in_region":True}
        )
        st.plotly_chart(scatter_fig)

    # Toevoegen van de boxplot voor videolengte per continent
    st.subheader("📊 Boxplot van Videolengte per Continent")

    color_sequence = px.colors.qualitative.Plotly
    fig = px.box(youtube,
                 x="continent",
                 y="duration_in_minutes",
                 color="continent",
                 color_discrete_sequence=color_sequence
                 )
    fig.update_layout(
        yaxis=dict(type="log"),
        title="Boxplot Videolengte per Continent",
        xaxis_title="Continent",
        yaxis_title="Duur in minuten (Log schaal)"
    )
    st.plotly_chart(fig)

    # Toevoegen van de top 5 categorieën per continent
    st.subheader("📊 Top 5 Categorieën per Continent")

    # Unieke continenten ophalen en sorteren
    continent_options = sorted(df["continent"].unique().tolist())

    # Toon de naam van het geselecteerde continent
    selected_continent = st.select_slider("Selecteer een continent:", options=continent_options, label_visibility = "collapsed")


    # Data filteren op het geselecteerde continent
    continent_data = df[df["continent"] == selected_continent]

    # Top 5 categorieën berekenen
    top_categories = (
        continent_data["category_name"]
        .value_counts(normalize=True)
        .nlargest(5)
        .reset_index()
    )
    top_categories.columns = ["category_name", "percentage"]
    top_categories["percentage"] *= 100

    # Bar chart maken
    category_fig = px.bar(
        top_categories,
        x="category_name",
        y="percentage",
        color="category_name",
        title=f"Top 5 Categorieën in {selected_continent}",
        labels={"category_name": "Categorie", "percentage": "Percentage van het totaal"},
        color_discrete_sequence=px.colors.qualitative.Plotly,
    )

    # Grafiek weergeven
    st.plotly_chart(category_fig)
        

#toevoegen scatterplot views en video lengte
    youtube = df.copy()
    
    continents = youtube["continent"].unique()
    continent_colors = {continent: i for i, continent in enumerate(continents)}
    youtube["continent_color"] = youtube["continent"].map(continent_colors)

    if youtube["views"].isna().sum() > 0 or youtube[y_axis_option].isna().sum() > 0:
        st.error("⚠ Er zitten ontbrekende waarden in de dataset, filter de data beter.")
    else:
        scatter_fig = px.scatter(
            youtube,
            x="duration_in_minutes",
            y="views",
            color="continent",
            color_discrete_sequence=px.colors.qualitative.Plotly,
            title=f"Views vs lengte van video per Continent",
            log_x=True,
            log_y=True,
            #trendline="ols",
            #trendline_color_override="black",
            hover_data={"title":True, "category_name":True,"country":True,"rank_in_region":True}
        )
        st.plotly_chart(scatter_fig)

        # Definieer de ranking groepen
    bins = list(range(1, 51, 5)) + [51]  # Zorg ervoor dat 50 wordt meegenomen
    labels = [f"{i}-{i+4}" for i in range(1, 50, 5)]
    
    df['rank_group'] = pd.cut(df['rank_in_region'], bins=bins, labels=labels, right=False)

    # Tel hoe vaak elke categorie in elke ranking-groep voorkomt
    grouped_counts = df.groupby(['rank_group', 'category_name']).size().unstack(fill_value=0).reset_index()

    # Streamlit UI
    st.title("Interactieve Ranking Analyse")
    st.write("Selecteer een categorie om de verdeling van rankings te bekijken.")

    # Dropdown-menu voor categorieën
    categories = df['category_name'].unique()
    selected_category = st.selectbox("Kies een categorie:", categories)

    # Filter data op geselecteerde categorie
    filtered_data = grouped_counts[['rank_group', selected_category]]
    filtered_data = filtered_data.rename(columns={selected_category: 'Aantal'})

    # Maak de plot
    fig = px.bar(
        filtered_data,
        x='rank_group',
        y='Aantal',
        labels={'rank_group': 'Ranking Groepen', 'Aantal': 'Aantal Voorkomen'},
        title=f'Aantal Voorkomen van Categorie {selected_category} per Ranking Groep',
        text_auto=True,
        )

    st.plotly_chart(fig)

# Functie voor de "Per continent" pagina
def per_continent():
    st.title("Per Continent - Selecteer Continent")
    df = load_video_data()
    Inputcontinent = st.sidebar.selectbox("Selecteer een continent", ("Europe", "Africa", "South America", "North America", "Oceania", "Asia"))
    youtubeselect = df[df["continent"] == Inputcontinent]
    st.dataframe(youtubeselect)

# Functie voor de "Per land" pagina
def per_land():
    st.title("Per Land - Selecteer een land")
    df = load_video_data()
    Inputcontinent = st.sidebar.selectbox("Selecteer een continent", ("Europe", "Africa", "South America", "North America", "Oceania", "Asia"))
    youtubeselect = df[df["continent"] == Inputcontinent]
    landen_in_continent = youtubeselect["country"].unique()
    Inputland = st.sidebar.selectbox("Selecteer een land", landen_in_continent)
    youtubeselect_land = youtubeselect[youtubeselect["country"] == Inputland]
    st.dataframe(youtubeselect_land)

# Functie voor de "Alle landen" pagina
def alle_landen():
    st.title("Alle Landen - Data Overzicht")
    df = load_video_data()
    st.dataframe(df)

PAGES = {
    "Overview": overview,
    "Alle landen": alle_landen,
    "Per continent": per_continent,
    "Per land": per_land
}

def show_page(page_name):
    page_function = PAGES.get(page_name)
    if page_function:
        page_function()

def main():
    page = st.sidebar.radio("Kies een pagina", list(PAGES.keys()))
    show_page(page)

if __name__ == "__main__":
    main()