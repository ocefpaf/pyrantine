series = temp.sel(time="2019").isel(
    s_rho=-1,
    eta_rho=42,
    xi_rho=42,
).to_array()

series.plot();
