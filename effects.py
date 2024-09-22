from pptx.oxml import parse_xml


def images_appear_on_click_effect(images, slide):
    # start ids for images and xml containers
    imgId = 2
    cTnID = 3
    xmlAlternateContent = """
<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">
    <mc:Choice xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" Requires="p14">
        <p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="slow" p14:dur="2000"></p:transition>
    </mc:Choice>
    <mc:Fallback>
        <p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="slow"></p:transition>
    </mc:Fallback>
</mc:AlternateContent>
"""
    xml = """
<p:timing xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">
<p:childTnLst><p:seq><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>
"""
    for img in images:
        xml += f"""
<p:par><p:cTn id="{cTnID}" fill="hold"><p:stCondLst>
<p:cond delay="indefinite" /></p:stCondLst><p:childTnLst>
<p:par><p:cTn id="{cTnID + 1}" fill="hold"><p:stCondLst>
<p:cond delay="0" /></p:stCondLst><p:childTnLst><p:par>

<p:cTn id="{cTnID + 2}" nodeType="clickEffect" fill="hold" presetClass="entr" presetID="1">
<p:stCondLst><p:cond delay="0" /></p:stCondLst>

<p:childTnLst><p:set><p:cBhvr><p:cTn id="{cTnID + 3}" dur="1" fill="hold">
<p:stCondLst><p:cond delay="0" /></p:stCondLst></p:cTn>
<p:tgtEl><p:spTgt spid="{imgId}"></p:spTgt></p:tgtEl>
<p:attrNameLst><p:attrName>style.visibility</p:attrName>
</p:attrNameLst></p:cBhvr><p:to><p:strVal val="visible" />
</p:to></p:set></p:childTnLst></p:cTn></p:par></p:childTnLst>
</p:cTn></p:par></p:childTnLst></p:cTn></p:par>
        """
        imgId += 1
        cTnID += 4

    xml += """
</p:childTnLst></p:cTn><p:prevCondLst><p:cond evt="onPrev">
<p:tgtEl><p:sldTgt /></p:tgtEl></p:cond></p:prevCondLst>
<p:nextCondLst><p:cond evt="onNext"><p:tgtEl><p:sldTgt />
</p:tgtEl></p:cond></p:nextCondLst></p:seq></p:childTnLst>
</p:cTn></p:par></p:tnLst></p:timing>
"""

    xmlFragmentAlternateContent = parse_xml(xmlAlternateContent)
    slide.element.insert(-1, xmlFragmentAlternateContent)
    xmlFragment = parse_xml(xml)
    slide.element.insert(-1, xmlFragment)


def images_appear_after_click_effect(images, delay, slide):
    # start ids for images and xml containers
    imgId = 2
    cTnID = 4
    sum_delay = 1

    xmlAlternateContent = """
<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">
    <mc:Choice xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" Requires="p14">
        <p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="slow" p14:dur="2000"></p:transition>
    </mc:Choice>
    <mc:Fallback>
        <p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="slow"></p:transition>
    </mc:Fallback>
</mc:AlternateContent>
"""
    xml = """
<p:timing xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">
<p:childTnLst><p:seq><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>
<p:par><p:cTn id="3" fill="hold"><p:stCondLst><p:cond delay="indefinite" /></p:stCondLst>
<p:childTnLst>
"""
    for i in range(len(images)):
        xml += f"""<p:par><p:cTn id="{cTnID}" fill="hold">"""
        if i == 0:
            xml += """<p:stCondLst><p:cond delay="0" /></p:stCondLst>"""
        else:
            xml += f"""<p:stCondLst><p:cond delay="{sum_delay}" /></p:stCondLst>"""

        xml += """<p:childTnLst><p:par>"""
        if i == 0:
            xml += f"""
<p:cTn id="{cTnID + 1}" nodeType="clickEffect" fill="hold" presetClass="entr" presetID="1">
<p:stCondLst><p:cond delay="0" /></p:stCondLst>
"""
        else:
            xml += f"""
<p:cTn id="{cTnID + 1}" nodeType="afterEffect" fill="hold" presetClass="entr" presetID="1">
<p:stCondLst><p:cond delay="{delay}" /></p:stCondLst>
"""
        xml += f"""
<p:childTnLst><p:set><p:cBhvr><p:cTn id="{cTnID + 2}" dur="1" fill="hold">
<p:stCondLst><p:cond delay="0" /></p:stCondLst></p:cTn>
<p:tgtEl><p:spTgt spid="{imgId}"></p:spTgt></p:tgtEl>
<p:attrNameLst><p:attrName>style.visibility</p:attrName>
</p:attrNameLst></p:cBhvr><p:to><p:strVal val="visible" />
</p:to></p:set></p:childTnLst></p:cTn></p:par></p:childTnLst>
</p:cTn></p:par>
        """
        imgId += 1
        cTnID += 3
        if i != 0:
            sum_delay += delay + 1

    xml += """
</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn>
<p:prevCondLst><p:cond evt="onPrev">
<p:tgtEl><p:sldTgt /></p:tgtEl></p:cond></p:prevCondLst>
<p:nextCondLst><p:cond evt="onNext"><p:tgtEl><p:sldTgt />
</p:tgtEl></p:cond></p:nextCondLst></p:seq></p:childTnLst>
</p:cTn></p:par></p:tnLst></p:timing>
"""

    xmlFragmentAlternateContent = parse_xml(xmlAlternateContent)
    slide.element.insert(-1, xmlFragmentAlternateContent)
    xmlFragment = parse_xml(xml)
    slide.element.insert(-1, xmlFragment)
    slide.element.remove_all("p:clrMapOvr")
