document.addEventListener("DOMContentLoaded", async function () {
    try {
        const response = await fetch("https://restcountries.com/v3.1/all");
        if (!response.ok) throw new Error("Erreur lors de la récupération des données");

        let countries = await response.json();

        // Trier les pays par ordre alphabétique
        countries.sort((a, b) => a.name.common.localeCompare(b.name.common));

        const countrySelect = document.getElementById("country");
        const countryCodeSelect = document.getElementById("country_code");

        countries.forEach(country => {
            const countryName = country.name.common;
            const countryCode = country.idd?.root + (country.idd?.suffixes ? country.idd.suffixes[0] : "");

            if (countryName && countryCode) {
                // Ajout des pays triés
                const countryOption = document.createElement("option");
                countryOption.value = countryName;
                countryOption.textContent = countryName;
                countrySelect.appendChild(countryOption);

                // Ajout des codes téléphoniques triés
                const codeOption = document.createElement("option");
                codeOption.value = countryCode;
                codeOption.textContent = `${countryCode} (${countryName})`;
                countryCodeSelect.appendChild(codeOption);
            }
        });

    } catch (error) {
        console.error("Erreur API:", error);
    }
});
