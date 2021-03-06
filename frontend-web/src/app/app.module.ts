import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { BucketComponent } from './bucket/bucket.component';
import { BucketDetailComponent } from './bucket-detail/bucket-detail.component';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { BucketSensorComponent } from './bucket-sensor/bucket-sensor.component';
import { SensorsComponent } from './sensors/sensors.component';

@NgModule({
    declarations: [
        AppComponent,
        BucketComponent,
        BucketDetailComponent,
        BucketSensorComponent,
        SensorsComponent
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        FormsModule
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule { }
