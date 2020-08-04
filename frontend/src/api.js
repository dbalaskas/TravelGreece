const listings_url = 'http://127.0.0.1:8000/api/v1/listings/';

export const fetchListings = async () => {
    return fetch(listings_url,{})
        .then(res => res.json())
        .then(data => {
            return data
        });
}

export const fetchListing = (id) => {
    return fetch(`${listings_url+id}`, {})
        .then(res => res.json())
        .then(data => {
            return data
        });
}

export const addListing = (listing) => {
    fetch(listings_url, {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(listing)
    })
    .then(res => res.json())
    .then(data => {
        console.log("Note:", data);
    })

    return listing;
}

export const update = (listing) => {
    console.log('We are updating..');
    console.log('Update a listing with id', listing.id);
}
