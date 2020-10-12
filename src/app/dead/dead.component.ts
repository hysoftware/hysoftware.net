import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-dead',
  styleUrls: ['./dead.component.scss'],
  templateUrl: './dead.component.html',
})
export class DeadComponent implements OnInit {

  @Input() public rip: number;

  constructor() { }

  ngOnInit() {
  }

}
