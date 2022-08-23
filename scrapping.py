from bing_image_downloader import downloader


class_name = ['A73EGS-p','acanthaluteres_brownii','acanthaluteres_spilomelanurus','acanthaluteres_vittiger','acanthistius_cinctus','acanthopagrus_australis','acanthopagrus_berda','acanthopagrus_latus','achoerodus_gouldii','achoerodus_viridis','acreichthys_tomentosus','aesopia_cornuta','aethaloperca_rogaa','alectis_ciliaris','alectis_indica','alepes_kleinii','aluterus_monoceros','aluterus_scriptus','amanses_scopas','anampses_caeruleopunctatus','anampses_elegans','anampses_femininus','anampses_geographicus','anampses_lennardi','anampses_melanurus','anampses_meleagrides','anampses_neoguinaicus','anampses_twistii','anodontostoma_chacunda','anyperodon_leucogrammicus','aphareus_furca','aphareus_rutilans','aprion_virescens','argyrops_spinifer','aseraggodes_melanostictus','atractoscion_aequidens','atule_mate','auxis_rochei','auxis_thazard','bathylagichthys_greyae','beryx_decadactylus','bodianus_anthioides','bodianus_axillaris','bodianus_bilunulatus','bodianus_bimaculatus','bodianus_diana','bodianus_loxozonus','bodianus_mesothorax','bodianus_perditio','bodianus_unimaculatus','bodianus_vulpinus','bothus_mancus','bothus_myriaster','bothus_pantherinus','brachaluteres_jacksonianus','brachirus_orientalis','caesioperca_lepidopterus','cantherhines_dumerilii','cantherhines_fronticinctus','cantherhines_pardalis']

for names in class_name:
    downloader.download(f"{names} fish", limit=15,  output_dir='./testData', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

