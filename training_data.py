# Format of training prompt
defaultPrompt = """I am an intelligent email assistant that can generate the following emails from the descriptive input:
Input: Vacsorához keresek helyet holnap este 8-ra a Benczúr utca közelében.

Output:
A holnap esti vacsorához az alábbi helyeket javaslom:
-


Input: Este 11-kor nyitva tartó éttermet keresek a Benczúr utca 11. 300 méteres körzetében.

Output:
Este 11-kor nyitva tartó éttermek listája a Benczúr utca 11 közelében:
-


Input: Kávézni szeretnénk a Damjanich utcában, növényi alapú tej és terasz előny.

Output:
Kávézáshoz ideális helyek a Damjanich utcában:
-


Input: A szív utcában van olyan kocsma, ahol van csapolt sör és enni is lehet?

Output:
Kocsmák a szív utca közelében, ahol enni is lehet:
-

Input: Hol lehet személyesen átvenni a rendelést?

Output:
Budapest, Fő u. 1.
-


Input: {}

Output: """