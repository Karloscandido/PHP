const options = {
  method: 'GET',
  headers: {accept: 'application/json', Authorization: 'sk_OPr7lJv8no8Z1lRm'}
};

fetch('https://api.short.io/api/links?domain_id=1085622&limit=150&beforeDate=2028-01-01T00%3A00%3A00.000Z&afterDate=2022-01-01T00%3A00%3A00.000Z&dateSortOrder=asc&pageToken=Split_sh', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));