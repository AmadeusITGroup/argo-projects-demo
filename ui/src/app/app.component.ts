import { CommonModule } from '@angular/common';
import { Component, ViewChild } from '@angular/core';

import {
  ApexAxisChartSeries,
  ApexChart,
  ChartComponent,
  ApexDataLabels,
  ApexPlotOptions,
  ApexYAxis,
  ApexTitleSubtitle,
  ApexXAxis,
  ApexFill,
  NgApexchartsModule
} from "ng-apexcharts";

import { PetService } from './pet.service';
import { animate } from '@angular/animations';

export type ChartOptions = {
  series: ApexAxisChartSeries;
  chart: ApexChart;
  dataLabels: ApexDataLabels;
  plotOptions: ApexPlotOptions;
  yaxis: ApexYAxis;
  xaxis: ApexXAxis;
  fill: ApexFill;
  title: ApexTitleSubtitle;
};

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, NgApexchartsModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {


  public buttonState = {
    label: "Start traffic",
    active: false
  }

  petStore = [0, 0, 0, 0]

  @ViewChild("chart") chart: ChartComponent;
  public chartOptions: Partial<ChartOptions>;

  
  constructor(private petService: PetService) {
    this.chartOptions = {
      series: [
        {
          name: "Number",
          data: this.petStore
        }
      ],
      chart: {
        height: 450,
        width: "50%",
        type: "bar",
        toolbar: {
          show: false
        },
        animations: {
          enabled: false
        }
      },
      plotOptions: {
        bar: {
          dataLabels: {
            position: "top" // top, center, bottom
          }
        }
      },
      dataLabels: {
        enabled: true,
        offsetY: -20,
        style: {
          fontSize: "12px",
          colors: ["#304758"]
        }
      },
      title: {
        text: "Pet retrieval transactions",
        floating: true,
        offsetY: 430,
        align: "center",
        style: {
          color: "#444"
        }
      },
      xaxis: {
        categories: ["😸", "🐶",  "🐦",  "💀"],        
        position: "top",
        offsetY: 60,
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        },
        labels: {
          offsetY: -18,
          style: {
            fontSize: "40px",
          }
        },
        tooltip: {
          enabled: false,
        }
      },
      yaxis: {
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        },
        labels: {
          show: false,
        }
      },
    };
    this.startFetchingPets();
  }

  public switchTraffic() {
    if (this.buttonState.active) {
      this.buttonState.active = false;
      this.buttonState.label = "Start traffic";
    } else {
      this.buttonState.active = true;
      this.buttonState.label = "Stop traffic";
    }
  }

  async startFetchingPets() {

    while (true) {
      await this.sleep(1000).then(() => { 
        if (this.buttonState.active) {
 
          console.log('Fetching pets!');
          this.petService.getPet().subscribe({

            next: (pet) => {
              switch(pet) { 
                case "Cat": { 
                  this.petStore[0] += 1;
                  break; 
                }
                case "Dog": { 
                  this.petStore[1] += 1;
                  break; 
                }
                case "Bird": { 
                  this.petStore[2] += 1;
                  break; 
                }
                default: { 
                  //discard 
                  break; 
                } 
              } 
              this.chart.updateSeries(
                [
                    {
                      name: "Number",
                      data: this.petStore
                    }
                ],
                true
              );
            },
            error: (e) => {
              console.error(e)
              this.petStore[3] += 1;
            }     
          })
        }
      })      
    }
  }

  private sleep(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

}
