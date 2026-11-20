# T5 – Caching și accelerarea accesului la date cu Redis

**StayFinder** este o platformă simplă de căutare a cazărilor (pe baza setului de date `sample_airbnb` din MongoDB Atlas). Utilizatorii pot căuta cazări, vedea detaliile unui anunț, topul celor mai bine cotate și cazări din apropiere, și pot pune întrebări unui asistent AI.

Redis este folosit ca nivel de cache între aplicație și MongoDB, pentru ca răspunsurile să vină mai rapid.
