package com.example.hashpath;

import retrofit2.Call;
import retrofit2.http.POST;
import retrofit2.http.Query;

public interface MainApi {

    @POST("signup")
    Call<GeoHash> signup(@Query("start") String username,
                         @Query("end") String end);

}
